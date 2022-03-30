import imp
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


class User:
    def __init__(self, data):
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = ''
        results = connectToMySQL(cls.db_name).query_db(query)
        return results