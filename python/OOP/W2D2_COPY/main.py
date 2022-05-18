from player import Player
from team import Team


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

devon = Player( {
    "name": "Devon Booker", 
    'is_active': True,
    "position": "Point Guard", 
    "total_points": 11217
})
chris = Player( {
    "name": "Chris Paul", 
    'is_active': True,
    "position": "Point Guard", 
    "total_points": 20936
})

nets = Team({
    't_name': 'Nets',
    'city': 'Brooklyn',
    'record': [3,2]
})
suns = Team({
    't_name': 'Suns',
    'city': 'Phoenix',
    'record': [5,1]
})

# kevin.team = nets
# kyrie.team = nets

suns.display_team_info()

# player_objs = Player.add_players(players)


# print(player_objs)
# nets.add_to_roster(Player.add_players(players))
# print(nets.roster)
# nets.display_team_info()
# kevin.team.display_team_info()
# nets.roster.append(kevin)
# nets.roster.append(kyrie)
# devon.play_game(35, nets)
# suns.roster.append(devon)
# devon.display_player_info()

# nets.display_team_info()