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

@app.route('/band/<int:id>')
def view_one_band_with_albums(id):
    # call to our view one with albums class method 
    # pass that into our html
    data ={ 
        'id': id
    }
    return render_template('one_band.html', this_band = band.Band.get_one_with_albums(data))

