from mysqlconnection import connectToMySQL

class User:
    db_name = "userscrud"
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(cls.db_name).query_db(query)
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users

    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (f_name, l_name, email) VALUES (%(f_name)s, %(l_name)s, %(email)s);'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results

    @classmethod
    def view_one(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(f"RESULTS: {results[0]}")
        this_user = cls(results[0])
        return this_user

    @classmethod
    def update_user(cls, data):
        query = 'UPDATE users SET f_name = %(f_name)s, l_name=%(l_name)s, email=%(email)s WHERE id=%(id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_user(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)