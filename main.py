from game.Player import Player
from game.Game import Game
from constants import BOARD_SIZE

playerA = Player("A")
playerB = Player("B")

game = Game(BOARD_SIZE, playerA, playerB)

# when winning move is at the end

# vertical
# game.play(0)
# game.play(1)
# game.play(0)
# game.play(1)
# game.play(0)
# game.play(1)
# win = game.play(0)

# horizontal
# game.play(0)
# game.play(0)
# game.play(1)
# game.play(1)
# game.play(2)
# game.play(2)
# win = game.play(3)

# diagnol
# game.play(0)
# game.play(1)
# game.play(1)
# game.play(2)
# game.play(2)
# game.play(3)
# game.play(2)
# game.play(4)
# game.play(3)
# game.play(3)
# win = game.play(3)

# when winning move is in the middle

# horizontal
# game.play(0)
# game.play(0)
# game.play(2)
# game.play(2)
# game.play(3)
# game.play(3)
# win = game.play(1)

# diagnol
# game.play(0)
# game.play(1)
# game.play(4)
# game.play(2)
# game.play(2)
# game.play(3)
# game.play(2)
# game.play(4)
# game.play(3)
# game.play(3)
# game.play(3)
# game.play(4)
# win = game.play(1)

game.print()
print(win)
