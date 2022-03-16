from flask_app import app
import os
from flask import render_template, redirect, request, session 
from ..models import user, recipe
from flask import flash
from werkzeug.utils import secure_filename

# Path to the uploads folder in the static folder I did it pathed to the static folder so it would be easier to access
UPLOADED_FOLDER = ('C:/Users/wilco/OneDrive/Desktop/flask-cohort-jason/flask_fullstack/recipes/flask_app/static/upload-image-for-recipes/')

# defining the types of files we accept
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOADED_FOLDER'] = UPLOADED_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/new/recipe") 
def new_recipe():
    return render_template('create_recipe.html')

@app.route('/create/recipe', methods=["POST"]) 
def create_recipe():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect('/new/recipe')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect('/new/recipe')
        if file and allowed_file(file.filename):
            print(UPLOADED_FOLDER)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOADED_FOLDER'], filename))
            print(f"this is line 34 : {UPLOADED_FOLDER}")

            data = {
                'name': request.form['name'],
                'ingredients': request.form['ingredients'],
                'instructions': request.form['instructions'],
                'date_made': request.form['date_made'],
                'under_30': request.form['under_30'],
                'image_path': "/static/upload-image-for-recipes/" + filename,
                'user_id': session['user_id']
            }
            print(data)
            recipe.Recipe.create_recipe(data)
    return redirect('/dashboard')

@app.route('/view/<int:recipe_id>') 
def view_one(recipe_id):
    data = {
        'id': recipe_id
    }
    this_recipe = recipe.Recipe.view_one(data)
    return render_template('view_one_recipe.html', this_recipe = this_recipe, x=0)

@app.errorhandler(404)
def not_found(e):
    return f'Bad URL' 
