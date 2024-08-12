from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Directory to save uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'gcode_file' not in request.files:
        return "No file part", 400

    file = request.files['gcode_file']

    if file.filename == '':
        continue  # Skip files without a name

    
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return f"File {file.filename} successfully uploaded!", 200

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)
