

class Coin:
    def __init__(self, data):
        self.id = data['uuid']
        self.name = data['name']
        self.icon = data['iconUrl']
        self.rank = data['rank']
        self.price = data['price']




    @classmethod
    def add_coins(cls, data):
        coins = []
        for coin in data:
            coins.append(cls(coin))
        return coins
    