from flask import Flask, render_template, request, send_from_directory, jsonify
import os
from PIL import Image
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
COMPRESSED_FOLDER = 'compressed'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['COMPRESSED_FOLDER'] = COMPRESSED_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def compress_and_optimize_image(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, optimize=True, quality=85)

    # Further optimize using ImageMagick (optional)
    subprocess.run(['convert', output_path, '-interlace', 'Plane', '-quality', '85%', output_path])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        filename = file.filename
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        output_path = os.path.join(app.config['COMPRESSED_FOLDER'], filename)
        
        try:
            # Compress and optimize the image
            compress_and_optimize_image(input_path, output_path)
            return jsonify({'message': 'File uploaded and compressed successfully', 'filename': filename})
        except Exception as e:
            return jsonify({'error': f'Error compressing {filename}: {e}'})

    return jsonify({'error': 'Invalid file format'})

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['COMPRESSED_FOLDER'], filename, as_attachment=True)

@app.route('/get_uploaded_files')
def get_uploaded_files():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify({'files': uploaded_files})

@app.route('/get_compressed_files')
def get_compressed_files():
    compressed_files = os.listdir(app.config['COMPRESSED_FOLDER'])
    return jsonify({'files': compressed_files})

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(COMPRESSED_FOLDER):
        os.makedirs(COMPRESSED_FOLDER)
    app.run(debug=True)
