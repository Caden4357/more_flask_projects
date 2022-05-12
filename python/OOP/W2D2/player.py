class Player:
    def __init__(self, data):
        self.name = data['name']
        self.position = data['position']
        self.is_active = data['is_active']
        self.total_points = data['total_points']
        self.team = None

    # This is an instance method it takes in self 
    def display_player_info(self):
        self.team.display_team_info()
        print(f'Name: {self.name}, Position: {self.position}, Team: The {self.team.t_name}, Total Career Points: {self.total_points}')

    def play_game(self, points_scored, opponent):
        self.total_points += points_scored
        print(f'{self.name} scored {points_scored} points against the {opponent.t_name}')

    @classmethod
    def add_players(cls,data):
        list_of_player_objs = []
        for dict in data:
            list_of_player_objs.append(cls(dict))
        return list_of_player_objs


