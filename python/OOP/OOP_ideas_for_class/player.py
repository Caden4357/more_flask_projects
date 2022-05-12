# The main idea here is to give students a look at classmethods staticmethods and instance methods in a way they are going to see in week 5 in week 2 of OOP 

# create a class this example is for NBA players
class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = None
    

    # * Creating class objects from a list of dictionaries
    # * this is pretty much what we are doing with a get all classmethod in full stack
    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects

    # *showing how to just create one player by passing in just a dictionary this isnt super neccesarry just added it for fun also might be good for them to see that since this is just one dictionary that will turn into one object we dont append it to a list or itterate through it to get the data its alreday a dict. 
    @classmethod
    def create_one_player(cls, data):
        this_player = cls(data)
        return this_player


    # * Passing in player_object which is a list of objects and displaying each players info 
    def display_players_info(player_object):
        for player in player_object:
            print("--------------------------")
            print(f"Name: {player.name}\nPosition: {player.position}\nTeam: {player.team}")


    # * Showing off an instance method not really anything special but open to ideas on more 
    def show_player_info(self):
        print(f'{self.name} is {self.age} years old and plays for the {self.team.city} {self.team.team_name}')



    # * this staticmethod is almost the same as one we would write in flask to validate our forms 
    @staticmethod
    def validate_player(data):
        is_valid = True
        output = ""
        for player in data:
            if len(player['name']) < 2:
                is_valid = False
                output += "name must be more than 2 characters\n"
            if player['age'] <= 17:
                is_valid = False
                output += "Players must be 18 or older\n"
            if len(player['position']) < 2:
                is_valid = False
                output += "position must be more than 2 characters\n"
            if len(player['team']) < 3:
                is_valid = False
                output += "Team must be more than 2 characters"
        print(output)
        return is_valid


# * this is here to show off create_one_player classmethod 
# kyrie_dict = {"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"}
# kyrie = Player.create_one_player(kyrie_dict)
# print(kyrie)
# print(kyrie.name)




# * a list of dictionaries is what comes back from sql querys in flask so its good to get them used to looking at this 
# players = [{"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"},{"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"},{"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"},{"name": "Damian Lillard", "age":33, "position": "Point Guard", "team": "Portland Trailblazers"},{"name": "Joel Embiid", "age":32, "position": "Power Foward", "team": "Philidelphia 76ers"},{"name": "", "age":16, "position": "P", "team": "en"}]


# valid = Player.validate_player(players)
# print(valid)
# print(players)

# player_objects = Player.add_players(players)

# * show the difference between the players and player_objects make note that players does not change its still just a list of dicts also not how to access key value pairs from a list of dictionaries is different than a list of objects 
# print(players)
# print(player_objects)
# print(players[0]['name'])
# print(player_objects[0].name)

# * calling the instance method 
# Player.change_name(player_objects[0], "Kevin Garnett")

# print("-------------Printing All Players-------------------")
# Player.display_players_info(player_objects)