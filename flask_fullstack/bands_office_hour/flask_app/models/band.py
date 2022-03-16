from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Band:
    db_name = "bands_schema"
    def __init__(self,data):
        self.id = data['id']
        self.band_name = data['band_name']
        self.origin = data['origin']
        self.year_formed = data['year_formed']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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





















# TALK TO JASON ABOUT THIS 

    # @classmethod
    # def get_all(cls):
    #     query = 'SELECT * FROM bands'
    #     results = connectToMySQL(cls.db_name).query_db(query)
    #     print(results)
    #     return results