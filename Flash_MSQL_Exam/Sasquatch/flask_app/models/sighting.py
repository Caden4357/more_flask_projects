from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Sighting:
    db = 'sasquatch_sch'

    def __init__(self,data):
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.num_of_sasquatch = data['num_of_sasquatch']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO sightings (location, description, num_of_sasquatch, date_made, user_id) VALUES (%(location)s,%(description)s,%(num_of_sasquatch)s,%(date_made)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sightings;"
        results = connectToMySQL(cls.db).query_db(query)
        all_sightings = []
        for row in results:
            print(row['date_made'])
            all_sightings.append( cls(row) )
        return all_sightings

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM sightings WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls,data):
        query = "UPDATE sightings SET location= %(location)s, description= %(description)s, num_of_sasquatch= %(num_of_sasquatch)s, date_made= %(date_made)s, updated_at= NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM sightings WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)


    @staticmethod
    def validate_sighting(sighting):
        is_valid = True
        if len(sighting['location']) < 3:
            is_valid = False
            flash("Location must be at least 3 characters", "sighting")
        if len(sighting['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters", "sighting")
        if int(sighting['num_of_sasquatch']) < int(1):
            is_valid = False
            flash("Can't report a sighting of 0!", "sighting")
        if len(sighting['date_made']) == "":
            is_valid = False
            flash("Please enter a date", "sighting")
        return is_valid
