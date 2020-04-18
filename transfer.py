import os
from flask import Flask
from flask import render_template
from flask import request, redirect
from flask import flash, url_for
import json

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route("/arqui")
def hello():
    return "Hello Arqui! This page is just for you!"

#@app.route("/<name>")
#def hello_name(name):
#    return "Hello " + name
    

@app.route('/upload', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect('/')
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect('/')
	if file and allowed_file(file.filename):
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		#flash('Image successfully uploaded and displayed')
		#return render_template('index.html', filename=file.filename)
		return redirect('/display/'+file.filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect('/')

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	#return redirect(url_for('static', filename='uploads/' + filename), code=301)
	url = url_for('static', filename='uploads/' + filename, _external=True)
	flash(url)
	flash('Copy & send the above url. Open it with a web browser. The file will be deleted in 24 hours.')
	return redirect('/')

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')

if __name__ == '__main__':
	app.run(port=5002,debug=False)
