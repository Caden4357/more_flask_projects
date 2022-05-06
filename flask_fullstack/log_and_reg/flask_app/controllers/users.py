from flask_app import app
from flask import render_template, redirect, request, session 
from ..models import user
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def create_owner():
    if not user.User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    user_info = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash,
    }
    new_user_id = user.User.create_user(user_info)
    session['user_id'] = new_user_id
    return redirect('/results')


@app.route('/login', methods=['POST'])
def login():
    # check if the user inputed anything 
    if not user.User.validate_login(request.form):
        flash('Please input email / password', 'login')
        return redirect('/')
    # check if the user is in the db based on the email in the form 
    user_from_db = user.User.get_by_email({'email':request.form['email']})
    
    # if email is in the db check the password from the form to the password for that user in the db


    # if both the above statements are true I want to log them in (save their id in session )
    if user_from_db and bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        session['user_id'] = user_from_db.id
        return redirect('/results')
    else:
        flash("Invalid email/password", 'login')
        return redirect('/')





@app.route('/results')
def results_page():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('dashboard.html', logged_in_user = user.User.get_by_id({'id': session['user_id']}))
























# @app.route('/login', methods=['POST'])
# def login():
#     if not user.User.validate_login(request.form):
#         flash('Please enter a valid email and password', "login")
#         return redirect('/')
#     # check if we have a user in the database with the email thats submitted in the form 
#     user_from_db = user.User.get_by_email({'email': request.form['email']})
#     # if we do have a user with that email we need to check the form password to the password for that user in the db 
#     if user_from_db and bcrypt.check_password_hash(user_from_db.password, request.form['password']):
#         session['user_id'] = user_from_db.id
#         return redirect('/results')
#     else:
#         flash('Invalid email/password', "login")
#         return redirect('/')




# @app.route('/login' , methods=['POST'])
# def login():
#     data = {
#         'email': request.form['email']
        
#     }
#     user_from_db = user.User.get_by_email(data)
#     if not user_from_db or not bcrypt.check_password_hash(user_from_db.password, request.form['password']) :
#         flash('Invalid email/password')
#         return redirect('/')
#     session['user_id'] = user_from_db.id
#     return redirect('/results')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')