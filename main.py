import src
print(f" I found src at: {src.__file__}")
from src.game import Game
from src.board import Board

if __name__ == '__main__':
    game = Game()
    game.play()
