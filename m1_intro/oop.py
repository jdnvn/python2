string = "this is a string"
integer = 1


def some_function():
    print("this is a function")


type(string)

type(number)


class Game:
    def __init__(self, players):
        self.players = players
    def list_players(self):
        for player in self.players:
            print(player.name, player.job)

class Player:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def fight(self):
        print(self.name + " is fighting")

player_1 = Player("emma", "fighter")
player_2 = Player("reyansh", "wizard")
player_3 = Player("jieni", "archer")
player_4 = Player("conor", "wizard")
player_5 = Player("joe", "fighter")

players = [player_1, player_2, player_3, player_4, player_5]
game = Game(players)
game.list_players()
