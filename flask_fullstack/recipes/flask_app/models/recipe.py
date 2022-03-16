from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from ..models import user

class Recipe:
    db_name="recipes_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ingredients = data['ingredients']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.image_path = data['image_path']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = []

    @classmethod
    def get_all(cls):
        query = 'SELECT recipes.id as id, recipes.name as food_name, recipes.ingredients as ingredients, recipes.instructions as instructions,recipes.under_30 as under_30, recipes.image_path as image_path, users.name as user_name, recipes.date_made as date_made FROM recipes JOIN users ON recipes.user_id = users.id;'
        results = connectToMySQL(cls.db_name).query_db(query)
        # recipes = []
        # for row in results:
        #     recipes.append(cls(row))
        return results

    @classmethod
    def create_recipe(cls, data):
        query = 'INSERT INTO recipes (name,ingredients, instructions, date_made, under_30, image_path, user_id) VALUES (%(name)s, %(ingredients)s, %(instructions)s, %(date_made)s, %(under_30)s, %(image_path)s, %(user_id)s);'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def view_one(cls, data):
        query = 'SELECT * FROM recipes WHERE id = %(id)s'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])