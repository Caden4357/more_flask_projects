from team import Team
from player import Player

# kevin = Player( {
#     "name": "Kevin Durant", 
#     'is_active': True,
#     "position": "Small Forward", 
#     "total_points": 25526
# })
# kyrie = Player( {
#     "name": "Kyrie Irving", 
#     'is_active': True,
#     "position": "Point Guard", 
#     "total_points": 14089
# })

players = [
    {
        "name": "Kyrie Irving", 
        "is_active": True,
        "position": "Point Guard", 
        "total_points": 14089
    },
    {
        "name": "Kevin Durant", 
        "is_active": True,
        "position": "Small Forward", 
        "total_points": 25526
    }
]


nets = Team({
    't_name': 'Nets',
    'city': 'Brooklyn',
    'record': [3,2]
})

player_objects = Player.add_players(players)
# print(player_objects[0].name)

# kevin.display_player_info()
# kevin.add_to_team(nets)
# kyrie.add_to_team(nets)
# kevin.team = 
# nets.roster.append(kevin)
# nets.roster.append(kyrie)
# nets.display_team_info()
# print(nets.roster)
# print(nets.roster[1].name)
# kevin.display_player_info()


