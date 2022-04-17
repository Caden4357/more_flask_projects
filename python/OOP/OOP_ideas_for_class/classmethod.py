
class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
    
    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects


players = [{"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}, {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"}]
print(players)
player_objects = Player.add_players(players)
print(players[0]['name'])
print(player_objects[0].name)
print("-------------Printing All Players-------------------")
for player in player_objects:
    print(f"Name: {player.name}\nPosition: {player.position}\nTeam: {player.team}")