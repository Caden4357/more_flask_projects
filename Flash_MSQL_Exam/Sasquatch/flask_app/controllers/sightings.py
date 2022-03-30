from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.sighting import Sighting
from flask_app.models.user import User

@app.route('/new/sighting')
def new_sighting():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("new_site.html", user = User.get_by_id(data))


@app.route('/create/sighting',methods=['POST'])
def create_sighting():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Sighting.validate_sighting(request.form):
        return redirect('/new/sighting')
    data = {
        "location": request.form["location"],
        "description": request.form["description"],
        "num_of_sasquatch": request.form["num_of_sasquatch"],
        "date_made": request.form["date_made"],
        "user_id": session["user_id"]
    }
    Sighting.save(data)
    return redirect('/dashboard')

@app.route('/edit/sighting/<int:id>')
def edit_sighting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit.html", edit = Sighting.get_one(data), user = User.get_by_id(user_data))

@app.route('/update/sighting',methods=['POST'])
def update_sighting():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Sighting.validate_sighting(request.form):
        return redirect('/new/sighting')
    data = {
        "location": request.form["location"],
        "description": request.form["description"],
        "num_of_sasquatch": request.form["num_of_sasquatch"],
        "date_made": request.form["date_made"],
        "id": request.form["id"]
    }
    Sighting.update(data)
    return redirect('/dashboard')

@app.route('/sighting/<int:id>')
def show_sighting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("sighting.html", sighting = Sighting.get_one(data), user = User.get_by_id(user_data))

@app.route('/destroy/sighting/<int:id>')
def destroy_sighting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Sighting.destroy(data)
    return redirect('/dashboard')