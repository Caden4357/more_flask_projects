
class Team:
    league = "USA"
    # season = 2022
    def __init__(self, data):
        self.t_name = data['t_name']
        self.city = data['city']
        self.record = data['record']
        self.roster = []

    def display_team_info(self):
        print(f'Team: The {self.city} {self.t_name} Record: Wins {self.record[0]} Losses {self.record[1]} \nRoster:')
        for player in self.roster:
            print(f'{player.name}')

    def add_to_roster(self,player_list):
        for player in player_list:
            self.roster.append(player)
        return self
        