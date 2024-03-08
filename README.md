# AutomatedImageCompression
Automated Image Compression and Optimization: Build a script to automatically compress and optimize images for web use, reducing file sizes without compromising image quality.

The compress_images function takes two arguments: input_dir (directory containing original images) and output_dir (directory where compressed and optimized images will be saved).
It iterates through each file in the input directory, checks if it's an image file, and compresses it using Pillow's save method with optimization enabled.
Optionally, you can further optimize images using ImageMagick by stripping metadata and setting interlace and quality settings.
Adjust the quality parameter according to your requirements. Higher values will result in better image quality but larger file sizes.
Ensure you have Pillow and ImageMagick installed in your Python environment (pip install pillow and ImageMagick installation).
Replace "input_images" and "output_images" with your input and output directory paths respectively.
Remember to always test your script on a small subset of images before running it on your entire image collection, to ensure that the compression settings meet your expectations. Additionally, always keep backups of your original images.

This Flask application has three routes:

/: This route renders the index.html template, which contains a file upload form.
/upload: This route handles the file upload process. It saves the uploaded file to the UPLOAD_FOLDER, compresses it, and saves the compressed version to the COMPRESSED_FOLDER.
/download/<filename>: This route allows users to download the compressed image by specifying its filename.
You need to create a template named index.html in a folder named templates, containing the HTML for the file upload form.

To run the application, save the code above to a Python file (e.g., app.py), and then run python app.py in your terminal. Access the application in your web browser at http://localhost:5000.
