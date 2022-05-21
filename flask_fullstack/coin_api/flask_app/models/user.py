

class User:
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.coin_wallet = []
        self.watchlist = []

    

    # ! ADD USER CRUD CLASSMETHODS 