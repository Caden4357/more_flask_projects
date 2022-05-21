from human import Human
from backpack import Backpack

class Warrior(Human):
    def __init__(self, data):
        super().__init__(data)
        self.strength = 20
        self.int = 2
        self.level = 10
        self.inventory = Backpack()

    def pickup_weapon(self, weapon):
        self.inventory.items.append(weapon)
        return self

    def show_inventory(self):
        for item in self.inventory.items:
            print(f'{item.name} Damage: {item.damage}')
        return self
    
    def weapon_attack(self,opponent):
        for item in self.inventory.items:
            if item.name == "Katana":
                if opponent.health - item.damage <= 0:
                    print('You died!')
                else:
                    opponent.health -= item.damage
                    print(f'{self.name} Attacked {opponent.name} for {item.damage} damage\nOpponents health: {opponent.health}')







