from game.Player import Player
from game.Game import Game
from constants import BOARD_SIZE

playerA = Player("A")
playerB = Player("B")

game = Game(BOARD_SIZE, playerA, playerB)
game.print()
print()
game.play(0, playerA)
game.print()
print()
game.play(0, playerB)
game.play(1, playerA)
game.play(1, playerA)
game.play(1, playerA)
win = game.play(1, playerA)
game.print()
print(win)
