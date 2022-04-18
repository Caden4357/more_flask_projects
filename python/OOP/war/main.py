from classes.human import Human
from classes.warrior import Warrior
from classes.backpack import Backpack
from classes.consumables import Consumable


# CREATING WARRIORS
# /////////////////////////////////////////////////////////////
chads_dict = {
    'name': "Chad The Bro",
    'age': 23,
}
jaxson_dict = {
    'name': "Jaxson The Mighty",
    'age': 33,
}

chad = Warrior(chads_dict)
# chad.level_up().birthday().display_info()
jaxson = Warrior(jaxson_dict)
# jaxson.display_info()
# chad.attack(jaxson)
# chad.display_info()
# chad.display_info().increase_stamina().display_info()
chad.attack(jaxson)
jaxson.display_info().heal().display_info()


# TESTING COSUMABLES/BACKPACK
# /////////////////////////////////////////////////////////////
hp_elx = {
    'id':1,
    'name': "health flask",
    'effects': "health",
    'effect_amount': 10,
    'effect_desc': "Found all over the place, consuming will increase health by 10"
}
stamina_elx = {
    'id':2,
    'name': "stamina flask",
    'effects': "stamina",
    'effect_amount': 10,
    'effect_desc': "Found all over the place, consuming will increase stamina by 10"
}
strength_boost_dict = {
    'id':3,
    'name': "stamina flask",
    'effects': "stamina",
    'effect_amount': 10,
    'effect_desc': "Found all over the place, consuming will increase stamina by 10"
}
stamina_elixir = Consumable(stamina_elx)
hp_elixir = Consumable(hp_elx)
strength_boost = Consumable(strength_boost_dict)
stamina_elixir.show_info()
jaxson.attack(chad).attack(chad)
chad.pickup_item(hp_elixir).pickup_item(stamina_elixir).pickup_item(hp_elixir).show_backpack_items().display_info().use_item(hp_elixir).show_backpack_items().display_info()
