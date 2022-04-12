from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import album


class Band:
    db_name = "bands_schema"
    def __init__(self,data):
        self.id = data['id']
        self.band_name = data['band_name']
        self.origin = data['origin']
        self.year_formed = data['year_formed']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.albums = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM bands'
        results = connectToMySQL(cls.db_name).query_db(query)
        all_bands = []
        for row in results:
            all_bands.append(cls(row))
        return all_bands

    @classmethod
    def create_band(cls, data):
        query = 'INSERT INTO bands (band_name, origin, year_formed) VALUES (%(band_name)s, %(origin)s, %(year_formed)s)'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def get_one_with_albums(cls,data):
        query = 'SELECT * FROM bands JOIN albums on bands.id = albums.band_id WHERE bands.id = %(id)s'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        this_band = cls(results[0])
        for row in results:
            album_data ={
                'id': row['albums.id'],
                'album_name': row['album_name'],
                'release_date': row['release_date'],
                'genre': row['genre'],
                'created_at': row['albums.created_at'],
                'updated_at': row['albums.updated_at'],
            }
            this_album = album.Album(album_data)
            this_band.albums.append(this_album)
        return this_band















































    # @classmethod
    # def get_one_band_with_albums(cls,data):
    #     query = 'SELECT * FROM bands JOIN albums ON bands.id = albums.band_id WHERE bands.id = %(id)s'
    #     results = connectToMySQL(cls.db_name).query_db(query, data)
    #     print(results)
    #     this_band = cls(results[0])
    #     print(results[0])
    #     print(this_band)
    #     for row in results:
    #         album_data = {
    #             'id':row['albums.id'],
    #             'album_name': row['album_name'],
    #             'release_date':row['release_date'],
    #             'genre': row['genre'],
    #             'created_at':row['albums.created_at'],
    #             'updated_at':row['albums.updated_at']
    #         }
    #         this_album = album.Album(album_data)
    #         this_band.albums.append(this_album)
    #     return this_band



















