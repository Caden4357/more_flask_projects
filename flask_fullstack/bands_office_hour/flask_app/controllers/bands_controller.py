from flask_app import app 
from flask import render_template, request, redirect
from ..models import band

@app.route('/') 
def index():
    all_bands = band.Band.get_all()
    return render_template('index.html', all_bands=all_bands)

@app.route('/new/band') 
def new_band():
    return render_template('new_band.html')

@app.route('/create/band', methods=['POST'])
def create_band():
    band.Band.create_band(request.form)
    return redirect('/')

@app.errorhandler(404)
def not_found(e):
    print(f'this is the type of e {type(e)}')
    return render_template('404_error.html', error=e)