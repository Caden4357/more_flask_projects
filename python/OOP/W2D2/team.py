

class Team:
    league = "USA"
    def __init__(self, data):
        self.t_name = data['t_name']
        self.city = data['city']
        self.record = data['record']
        self.roster = []


    def display_team_info(self):
        print(f'The {self.city} {self.t_name} Record Wins: {self.record[0]} losses: {self.record[1]} Roster:')
        for player in self.roster:
            print(player.name)
        return self
    

