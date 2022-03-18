from flask_app.config.mysqlconnection import connectToMySQL

class Image:
    db_name = "image_test_schema"
    def __init__(self, data):
        self.id = data['id']
        self.image_path = data['image_path']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM images;'
        results = connectToMySQL(cls.db_name).query_db(query)
        all_images=[]
        for row in results:
            all_images.append(cls(row))
        return all_images

    @classmethod
    def create_image(cls,data):
        query = 'INSERT INTO images (image_path, description) VALUES (%(image_path)s, %(description)s);'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results










































# from flask_app.config.mysqlconnection import connectToMySQL
# from flask import flash
# import re

# class Image:
#     db_name="image_test_schema"
#     def __init__(self, data):
#         self.id = data['id']
#         self.image_path = data['image_path']
#         self.description = data['description']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']

#     @classmethod
#     def get_all(cls):
#         query = 'SELECT * FROM images'
#         results = connectToMySQL(cls.db_name).query_db(query)
#         all_images = []
#         for row in results:
#             all_images.append(cls(row))
#         return all_images

#     @classmethod
#     def create_image(cls, data):
#         query = 'INSERT INTO images (image_path, description) VALUES (%(image_path)s, %(description)s);'
#         results = connectToMySQL(cls.db_name).query_db(query,data)
#         return results