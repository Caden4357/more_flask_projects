from flask_app import app 
from flask import render_template, jsonify, request, redirect
from ..models import band, album

@app.route('/new/album') 
def new_album():
    return render_template('new_album.html', all_bands=band.Band.get_all())

@app.route('/create/album', methods=['POST'])
def create_album():
    # form_info is a dict we send to the models this becomes the 'data' dict in our classmethod just under that different name (usually data)
    form_info = {
        'album_name': request.form['album_name'],
        'release_date': request.form['release_date'],
        'genre': request.form['genre'],
        'band_id': request.form['band_id']
    }   
    album.Album.create_album(form_info)
    return redirect('/')


