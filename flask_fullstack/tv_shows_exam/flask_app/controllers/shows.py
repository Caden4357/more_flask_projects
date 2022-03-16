from flask_app import app 
from flask import render_template, request, redirect, session
from ..models import show

@app.route('/add/show') 
def add_show():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('add_show.html')

@app.route('/create/show', methods=["POST"]) 
def create_show():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'title': request.form['title'],
        'network': request.form['network'],
        'description': request.form['description'],
        'release_date': request.form['release_date'],
        'user_id': session['user_id'],
    }
    show.Show.create_show(data)
    return redirect('/dashboard')

@app.route('/view_one/<int:id>')
def view_one(id):
    data = {
        'id':id
    }
    this_show = show.Show.get_one_tv_show_with_all_users_who_liked_it(data)
    return render_template("one_show.html", this_show=this_show)

@app.route('/add_like/<int:show_id>')
def add_like(show_id):
    data={
        'user_id': session['user_id'],
        'show_id': show_id
    }
    show.Show.like_tv_show(data)
    return redirect('/dashboard')

@app.errorhandler(404)
def not_found(e):
    return f'Bad URL' 