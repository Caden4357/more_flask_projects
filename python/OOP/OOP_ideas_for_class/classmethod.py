
class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
    

    # Creating class objects from a list of dictionaries
    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects


    @classmethod
    def create_one_player(cls, data):
        return cls(data)

    @staticmethod
    def display_players_info(player_object):
        for player in player_object:
            print("--------------------------")
            print(f"Name: {player.name}\nPosition: {player.position}\nTeam: {player.team}")

    # Instance method
    def change_name(self, val):
        self.name = val
        return self


# kyrie_dict = {"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"}
# kyrie = Player.create_one_player(kyrie_dict)
# print(kyrie)
# print(kyrie.name)


players = [{"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"},{"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"},{"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"}]

# print(players)

player_objects = Player.add_players(players)

# print(player_objects)
# print(players[0]['name'])
# print(player_objects[0].name)

Player.change_name(player_objects[0], "Kevin Garnett")

print("-------------Printing All Players-------------------")
Player.display_players_info(player_objects)
# for player in player_objects:
#     print(f"Name: {player.name}\nPosition: {player.position}\nTeam: {player.team}")