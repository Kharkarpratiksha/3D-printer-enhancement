from flask import Flask, request, render_template, redirect, url_for

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
        return "No selected file", 400  # Return an error if the file has no name
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    return f"File {file.filename} successfully uploaded!", 200

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Get email and password from the form
        email = request.form.get('email')  # Changed from 'username' to 'email'
        password = request.form.get('password')

        if email and password:
            # Here you would normally check the username and password
            # (Perform authentication logic here)

            return redirect(url_for('index'))  # Redirect to home page after sign in
        else:
            return "Invalid credentials", 400  # Return an error if email or password is missing
    
    return render_template('signin.html')



# Status Page
@app.route('/status')
def status():
    return render_template('status.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)
