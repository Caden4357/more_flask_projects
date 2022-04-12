from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import band

class Album:
    db_name = "bands_schema"
    def __init__(self, data):
        self.id = data['id']
        self.album_name = data['album_name']
        self.release_date = data['release_date']
        self.genre = data['genre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.band = None

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM albums JOIN bands ON albums.band_id = bands.id;'
        results = connectToMySQL(cls.db_name).query_db(query)
        print(results)
        all_albums = []
        for row in results:
            this_album = cls(row)
            band_data = {
                'id': row['bands.id'],
                'band_name': row['band_name'],
                'origin': row['origin'],
                'year_formed': row['year_formed'],
                'created_at': row['bands.created_at'],
                'updated_at': row['bands.updated_at'],
            }
            this_band = band.Band(band_data)
            this_album.band = this_band
            all_albums.append(this_album)
        return all_albums

    @classmethod
    def create_album(cls, data):
        query = 'INSERT INTO albums (album_name, release_date, genre, band_id) VALUES (%(album_name)s, %(release_date)s, %(genre)s, %(band_id)s)'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results
