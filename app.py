from flask import Flask, render_template, request
from PIL import Image
from colors import extract_colors, make_css_pallete
from io import BytesIO

app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('upload.html')
 
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Get the uploaded file from the request
        file = request.files['image']
 
        # Read the file into a PIL Image object
        bytes_img = file.read()
        f = BytesIO(bytes_img)
        f.seek(0)
        img = Image.open(f)
 
        # Extract colors from the image using the extract_colors function
        colors_dict = extract_colors(img)
        print(colors_dict)
 
        # Generate a CSS file with custom properties for each color in the palette
        css = make_css_pallete(colors_dict['colors'])
        # Render a template with the color palette displayed as circular swatches using CSS
        return render_template('result.html', colors=colors_dict['colors'], css=css)
