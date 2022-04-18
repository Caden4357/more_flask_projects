
class Human:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.level = 5
        self.health = 100
        self.max_health = 100
        self.stamina = 20
        self.strength = 10
        

    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nStrength: {self.strength}\nStamina: {self.stamina}\nHealth: {self.health}\nLevel: {self.level}")
        return self

    def birthday(self):
        self.age += 1 
        print(f'another year has past your {self.age} years old celebrate with a pint')
        return self

    def eat(self):
        if self.health == self.max_health:
            print("Your at full health")
        elif self.health + 5 > self.max_health:
            self.health = self.max_health
        else:
            self.health += 5
        return self

    def meditate(self):
        self.stamina += 5
        return self
    


