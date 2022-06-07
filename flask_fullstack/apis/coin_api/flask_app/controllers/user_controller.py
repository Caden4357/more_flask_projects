from tkinter import E
from flask import Flask, render_template,redirect,jsonify,request,session
from flask_app import app, db
import requests
from flask_app.models.tables import User, Purchase
from flask_login import LoginManager, login_manager, UserMixin, login_required, login_user, logout_user, current_user
login_manager = LoginManager()
login_manager.init_app(app)
# ! ADD BCRYPT 

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

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
    # db.session.add(new_user)
    user = db.session.add(new_user)
    # login_user(user)
    # print(user)
    result = db.session.commit()
    email = request.form['email']
    print(email)
    this_user = User.query.filter_by(email=email).first()
    print(f"THIS IS USER: {this_user.id} {this_user.first_name} {this_user.last_name}")
    return redirect('/home')

@app.route('/login')
def login():
    pass