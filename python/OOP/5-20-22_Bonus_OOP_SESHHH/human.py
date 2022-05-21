
class Human:
    def __init__(self, data):
        self.name = data['name']
        self.health = 100
        self.strength = 10
        self.int = 4
        self.stamina = 50
        self.level = 5
        self.xp = 0

    def display_info(self):
        print(f"{self.name}\nLevel: {self.level}\nStrength: {self.strength}\nIntelligence: {self.int}\nHealth: {self.health}\nStamina: {self.stamina}")
        return self
    
    def level_up(self):
        self.health += 10
        self.strength += 5
        self.level += 1 
        self.int += 2
        return self

    def attack(self,opponent):
        if (opponent.health - self.strength) <= 0:
            print('You died!')
        else:
            opponent.health -= self.strength
            print(f'{self.name} Attacked {opponent.name} for {self.strength} damage\nOpponents health: {opponent.health}')
        return self

