from game.games import PacmanGame
from game.search import *
from game.player import *

game = PacmanGame(board=5)
print(game.draw_board(game.init_state()))
# first_player = Random(game=game)
first_player = LimitedAlphaBeta(game=game, limit=20)
# first_player = Custom(game)
# second_player = Random(game=game)
second_player = LimitedAlphaBeta(game=game, limit=20)

moves = game.play(first_player, second_player)

print(moves)

