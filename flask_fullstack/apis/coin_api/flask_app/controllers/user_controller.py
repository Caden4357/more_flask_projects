from tkinter import E
from flask import Flask, render_template,redirect,jsonify,request,session
from flask_app import app, db
import requests
from flask_app.models.tables import User, Purchase
from flask_login import LoginManager, login_manager, UserMixin, login_required, login_user, logout_user, current_user
login_manager = LoginManager()
login_manager.init_app(app)
# ! ADD BCRYPT 


# ! LEARN MORE ABOUT THIS HOW IS IT WORKING?
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@app.route('/register/login')
def register_login():
    return render_template('sign_in_up.html')

@app.route('/register/user', methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/register/login')
    # ! ADD PASSWORD HASH 
    # ! HOW DO WE GET THE NEW USERS ID IN SESSION? SEEMS LIKE WE NEED FLASK LOGIN 
    new_user = User(first_name = request.form['first_name'], last_name = request.form['last_name'], email = request.form['email'], password = request.form['password'])
    email = request.form['email']
    print(email)

    # ! I'm sure this can be revised 
    this_user = User.query.filter_by(email=email).first()
    login_user(this_user)

    # this is actually adding it the db you need .add() followed by .commit() everytime 
    db.session.add(new_user)
    db.session.commit()
    print(f"THIS IS USER: {this_user.id} {this_user.first_name} {this_user.last_name}")
    return redirect('/home')


# ! FIGURE OUT LOGGING IN AND OUT 
@app.route('/login')
def login():
    pass

@app.route('/logout')
def logout():
    pass