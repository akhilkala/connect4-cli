from game.Player import Player
from game.Game import Game
from constants import BOARD_SIZE

playerA = Player("A")
playerB = Player("B")

game = Game(BOARD_SIZE, playerA, playerB)

# when winning move is at the end

# vertical
# game.play(0, playerA)
# game.play(0, playerA)
# game.play(0, playerA)
# win = game.play(0, playerA)

# horizontal
# game.play(0, playerA)
# game.play(1, playerA)
# game.play(2, playerA)
# win = game.play(3, playerA)

# diagnol
# game.play(0, playerA)
# game.play(1, playerA)
# game.play(1, playerA)
# game.play(2, playerB)
# game.play(2, playerB)
# game.play(2, playerA)
# game.play(3, playerB)
# game.play(3, playerB)
# game.play(3, playerB)
# win = game.play(3, playerA)

# when winning move is in the middle

# horizontal
# game.play(0, playerA)
# game.play(2, playerA)
# game.play(3, playerA)
# win = game.play(1, playerA)

# diagnol
# game.play(0, playerA)
# game.play(1, playerA)
# game.play(3, playerA)
# game.play(2, playerB)
# game.play(2, playerB)
# game.play(1, playerA)
# game.play(3, playerB)
# game.play(3, playerB)
# game.play(3, playerA)
# win = game.play(2, playerA)

game.print()
print(win)
