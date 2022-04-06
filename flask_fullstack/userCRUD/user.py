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
    def get_one(cls, data_to_query):
        query = 'SELECT * FROM users WHERE id = %(user_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query,data_to_query)
        print(f"RESULTS: {results}")
        print(f"RESULTS: {cls(results[0])}")
        return cls(results[0])

    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (f_name, l_name, email) VALUES (%(f_name)s, %(l_name)s, %(email)s);'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results
        

    @classmethod
    def update(cls, data):
        query = 'UPDATE users SET f_name=%(f_name)s, l_name=%(l_name)s, email=%(email)s WHERE id = %(id)s'
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return results

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users WHERE id =%(id)s'
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return results