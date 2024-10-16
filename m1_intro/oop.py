string = "this is a string"
integer = 1


def some_function():
    print("this is a function")


type(string)

type(integer)


class Game:
    def __init__(self, players):
        self.players = players
    def list_players(self):
        for player in self.players:
            print(player.name, player.type)

class Player:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def fight(self):
        if self.type == "fighter":
            print("Slash!")
        elif self.type == "wizard":
            print("FIREBALL")
        elif self.type == "archer":
            print("shoot an arrow ->")

player_1 = Player("emma", "fighter")
player_2 = Player("reyansh", "wizard")
player_3 = Player("jieni", "archer")
player_4 = Player("conor", "wizard")
player_5 = Player("joe", "fighter")

players = [player_1, player_2, player_3, player_4, player_5]
game = Game(players)
game.list_players()


# INHERITANCE

class Player:
    def __init__(self, name):
        self.name = name

    def fight(self):
        print("You can't fight")


class Knight(Player):
    def __init__(self, name):
        self.name = name

    def fight(self):
        print("Slash!")


class Healer(Player):
    def __init__(self, name):
        self.name = name

    def heal(self, player):
        print(f"{self.name} is healing {player.name}")


jieni = Knight("jieni")
reyansh = Healer("reyansh")
reyansh.heal(jieni)


# aside: F-strings
num_dogs = 5
num_dogs_str = str(num_dogs)
non_f_string = "There are " + num_dogs_str + " dogs"
f_string = f'There are {num_dogs_str} dogs'