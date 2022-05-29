from flask import Flask, render_template,redirect,jsonify,request,session
from flask_app import app, db
import requests
from flask_app.models.tables import User, Purchase
# ! ADD BCRYPT 

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
    # print(new_user.id)
    result = db.session.commit()
    print(result)
    return redirect('/home')