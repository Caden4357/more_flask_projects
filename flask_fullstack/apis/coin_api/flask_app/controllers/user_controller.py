from flask import Flask, render_template,redirect,jsonify,request,session
from flask_app import app, db
import requests
from flask_app.models.tables import User, Purchase

@app.route('/register/login')
def register_login():
    return render_template('sign_in_up.html')

@app.route('/register/user', methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/register/login')
    new_user = User(first_name = request.form['fist_name'], last_name = request.form['last_name'], email = request.form['email'], password = request.form['password'])
    db.session.add(new_user)
    db.session.commit()
    return redirect('/home')