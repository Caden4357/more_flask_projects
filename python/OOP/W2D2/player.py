# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team


# kevin = Player("kevin Durant", 34, "small forward", "brooklyn nets")


# kevin = Player({
#     "name": "Kevin Durant", 
#     "age":34, 
#     "position": "small forward", 
#     "team": "Brooklyn Nets"
# })


class Player:
    def __init__(self, data):
        self.name = data['name']
        self.position = data['position']
        self.is_active = data['is_active']
        self.total_points = data['total_points']
        self.team = None

    def display_player_info(self):
        print(f'{self.name} plays {self.position} for the {self.team.t_name} and has {self.total_points} total career points')
        return self

    def add_to_team(self,franchise):
        self.team = franchise
        franchise.roster.append(self)
        return self

    @classmethod
    def add_players(cls, data):
        lst_of_players = []
        for player in data:
            this_player = cls(player)
            lst_of_players.append(this_player)
        return lst_of_players




