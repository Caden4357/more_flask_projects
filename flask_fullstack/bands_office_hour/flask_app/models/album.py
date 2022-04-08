from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

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
        query = 'SELECT * FROM albums'
        results = connectToMySQL(cls.db_name).query_db(query)
        return results

    @classmethod
    def create_album(cls, data):
        query = 'INSERT INTO albums (album_name, release_date, genre, band_id) VALUES (%(album_name)s, %(release_date)s, %(genre)s, %(band_id)s)'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results
