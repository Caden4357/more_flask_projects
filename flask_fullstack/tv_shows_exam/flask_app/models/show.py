from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Show:
    db_name = "tv_show_schema"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.description = data['description']
        self.release_date = data['release_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.user_who_posted = {}
        self.user_who_posted = User.get_by_id({'id': data['user_id']})
        self.users_who_like = []
        # self.user_who_posted = []


    # @classmethod
    # def get_all(cls):
    #     query = 'SELECT * FROM shows JOIN users on users.id = shows.user_id;'
    #     results = connectToMySQL(cls.db_name).query_db(query)
    #     all_shows=[]
    #     if len(results) > 0:
    #         for row in results:
    #             show_data = {
    #                 'id': row['id'],
    #                 'title': row['title'],
    #                 'network': row['network'],
    #                 'description': row['description'],
    #                 'release_date': row['release_date'],
    #                 'created_at': row['created_at'],
    #                 'updated_at': row['updated_at'],
    #             }
    #             user_data = {
    #                 'id': row['users.id'],
    #                 'first_name': row['first_name'],
    #                 'last_name': row['last_name'],
    #                 'email': row['email'],
    #                 'password': row['password'],
    #                 'created_at': row['users.created_at'],
    #                 'updated_at': row['users.updated_at']
    #             } 
    #             show = Show(show_data)
    #             user = User(user_data)
    #             show.user_who_posted = user
    #             # show.user_who_posted.append(user)
    #             all_shows.append(show)
    #             print(show.user_who_posted.first_name)
    #             #<td>{{ show.user_who_posted[0].first_name}}</td>
    #     return all_shows


    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM shows JOIN users on users.id = shows.user_id;'
        results = connectToMySQL(cls.db_name).query_db(query)
        all_shows=[]
        if len(results) > 0:
            for row in results:
                this_show = cls(row)
                print(this_show.title)
                user_data = {
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                } 
                user = User(user_data)
                this_show.user_who_posted = user
                # show.user_who_posted.append(user)
                all_shows.append(this_show)
                print(this_show.user_who_posted.first_name)
        return all_shows


    @classmethod
    def create_show(cls,data):
        query = 'INSERT INTO shows (title, network, description, release_date, user_id) VALUES (%(title)s,%(network)s,%(description)s,%(release_date)s,%(user_id)s)'
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return results

    @classmethod
    def get_one_tv_show_with_all_users_who_liked_it(cls,data):
        # query = 'SELECT * FROM shows JOIN users on users.id = shows.user_id WHERE shows.id = %(id)s'
        query = "SELECT * FROM shows JOIN likes ON shows.id = likes.show_id JOIN users ON users.id = likes.user_id WHERE shows.id = %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # data = results[0]
        this_show = cls(results[0])
        print(this_show.title)
        # print(f"RESULTS: {results[0]['users.id']}")
        for row in results:
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            this_user = User(user_data)
            this_show.users_who_like.append(this_user)
        # this_user = User(user_data)
        # this_show.user_who_posted = this_user
        return this_show

    @classmethod
    def like_tv_show(cls,data):
        query = 'INSERT INTO likes (user_id, show_id) VALUES (%(user_id)s, %(show_id)s)'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    
    @classmethod
    def unlike_tv_show(cls,data):
        query = 'INSERT INTO likes (user_id, show_id) VALUES (%(user_id)s, %(show_id)s)'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results