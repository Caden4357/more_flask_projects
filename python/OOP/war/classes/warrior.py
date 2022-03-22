from classes.human import *
from classes.backpack import Backpack

class Warrior(Human):
    def __init__(self, data, strength=25):
        super().__init__(data, strength)
        self.level = data['level']
        self.backpack = Backpack()
    
    def display_info(self):
        self.info()
        return self
    
    def heal(self):
        self.eat()
        return self
    
    def increase_stamina(self):
        self.meditate()
        return self

    def level_up(self):
        self.level += 1
        self.strength += 5 
        self.health += 5
        print(f"leveled up strength and health your are now level {self.level}")
        return self 
    
    def attack(self, opponent):
        attack_power = self.strength // 4
        if opponent.health - attack_power <= 0:
            opponent.health = 0
            print(f"Noble warrior {self.name} has fallen")
        else: opponent.health -= attack_power
        print(f"{self.name} attacked {opponent.name} for {attack_power} damage {opponent.name}'s health is now: {opponent.health}")
    
    def pickup_item(self, item):
        self.backpack.add_item(item)
        return self
    
    def show_backpack_items(self):
        print(f"Showing {self.name}'s backpack:")
        self.backpack.show_backpack()
        return self

    def use_item(self, item):
        if item.name == "health flask":
            # if item.effect_amount + self.health < 
            self.health += item.effect_amount
        self.backpack.consum_item(item)
        return self