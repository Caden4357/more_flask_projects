from warrior import Warrior
from weapon import Weapon
# from human import Human

katana = Weapon({'name': 'Katana', 'damage': 30})
mace = Weapon({'name': 'Mace', 'damage': 15})
bob = Warrior({'name': 'Bob Ross'})
rodgers = Warrior({'name': 'Mr. Rodgers'})
bob.pickup_weapon(katana)
rodgers.pickup_weapon(mace)
# bob.attack(rodgers).attack(rodgers).attack(rodgers).attack(rodgers).attack(rodgers)
bob.weapon_attack(rodgers)
# bob.show_inventory()
# bob.level_up()
# bob.display_info()