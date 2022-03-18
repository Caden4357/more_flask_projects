from flask_app import app 
from flask import render_template, request, redirect, flash
import os
from werkzeug.utils import secure_filename
from ..models import image

UPLOAD_FOLDER = 'C:/Users/wilco/OneDrive/Desktop/flask-cohort-jason/flask_fullstack/image_upload_test/flask_app/static/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/') 
def index():
    return render_template('index.html', all_images=image.Image.get_all())

@app.route('/post/image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect('/')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect('/')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)
            data = {
                'image_path': "/static/images/"+filename,
                'description': request.form['description']
            }
            image.Image.create_image(data)
        return redirect('/')













































# from flask_app import app 
# import os
# from werkzeug.utils import secure_filename
# from flask import render_template, jsonify, request, redirect, flash
# from ..models import image

# UPLOAD_FOLDER = ('C:/Users/wilco/OneDrive/Desktop/flask-cohort-jason/flask_fullstack/image_upload_test/flask_app/static/images/')

# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# def allowed_file(filename):
#     return '.' in filename and \
#         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/') 
# def index():
#     all_images=image.Image.get_all()
#     return render_template('index.html', all_images=all_images)

# @app.route('/post/image', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # If the user does not select a file, the browser submits an
#         # empty file without a filename.
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             print(filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             data = {
#                 'image_path': '/static/images/' + filename,
#                 'description': request.form['description']
#             }
#             image.Image.create_image(data)
#         return redirect('/')