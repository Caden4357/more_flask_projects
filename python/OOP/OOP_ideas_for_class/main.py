from player import Player
from team import Team

kevin = Player({'name': 'Kevin Durant', 'age': 34, 'position':'Forward'})
nets = Team({'team_name': 'Nets', 'city': 'Brooklyn', 'origin': 1967})
kevin.team = nets
# kevin.team.team_name
kevin.show_player_info()