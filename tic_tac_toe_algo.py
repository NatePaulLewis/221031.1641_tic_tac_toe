# TIC TAC TOE

board = [
    9, 8, 7,
    6, 5, 4,
    3, 2, 1
]

winning_numbers = [
[9, 8, 7],
[6, 5, 4],
[3, 2, 1],
[9, 6, 3],
[8, 5, 2],
[7, 4, 1],
[9, 5, 1],
[7, 5, 3]
]

player_x = [9, 4, 6, 3]
player_o = []

class TicTacToe:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def __repr__(self):
        return "%s's Testing this out to see if it works" % (self.player1, self.player2, self.player_x, self.player_O)
        # return "%s's Account Balance: $%.2f" % (self.name, self.balance)

    def winner_check(self, ls1, ls2):
        for i in ls1:
            i.sort()
            x = set(ls2).intersection(i)
            x = list(x)
            x.sort()
            if i == x:
                print(True)
            else:
                print(False)


game = TicTacToe('Nate', 'Chris')
game.winner_check(winning_numbers, player_x)


# for i in winning_numbers:
#     i.sort()
#     x = set(player_x).intersection(i)
#     x = list(x)
#     x.sort()
#     if i == x:
#         print(True)
#     else:
#         print(False)


