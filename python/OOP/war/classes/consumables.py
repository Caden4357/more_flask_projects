

class Consumable:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.effects = data['effects']
        self.effect_amount = data['effect_amount']
        self.effect_desc = data['effect_desc']

    def show_info(self):
        print(f'Name: {self.name}\nDescription:{self.effect_desc}')
        return self