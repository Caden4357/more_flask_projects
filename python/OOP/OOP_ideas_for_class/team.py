
class Team:
    def __init__(self,data):
        self.team_name = data['team_name']
        self.city = data['city']
        self.origin = data['origin'] # Is just the year the franchise was founded ex. 1984
        # self.roster = []
    
    @classmethod
    def add_team(cls, data):
        this_team = cls(data)
        return this_team

    # instance method 
    def add_player(self,player):
        self.roster.append(player)
