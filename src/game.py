from src.board import Board
from src.player import Player, Computer

class Game:

    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.current_player = None

    def setup_game(self):
        print("=" * 40)
        print("    CONNECT FOUR")
        print("=" * 40)
        print()

        print("Spielmodus wählen:")
        print("  (1) Player vs Player")
        print("  (2) Player vs Computer")
        print()

        modus = input("Choose (1 or 2): ")
        print()


        if modus == '2':
            name = input("Your name: ")
            self.player1 = Player(name, 'X')
            self.player2 = Computer("Computer", 'O')

        else:
            name1 = input("Name Spieler 1: ")
            name2 = input("Name Spieler 2: ")
            self.player1 = Player(name1, 'X')
            self.player2 = Player(name2, 'O')

        self.current_player = self.player1

        print()
        print(f"{self.player1.name} is playing as '{self.player1.symbol}'")
        print(f"{self.player2.name} is playing as '{self.player2.symbol}'")
        print()

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play(self):
        self.setup_game()

        while True:
            self.board.display()
            print()

            column = self.current_player.get_move(self.board)

            if column == -1:
                print()
                print("Game Over!")
                break

            success = self.board.drop_stone(column, self.current_player.symbol)

            if not success:
                print()
                print("This column is full, choose another one.")
                print()
                continue

            if self.board.check_win(self.current_player.symbol):
                self.board.display()
                print()
                print("=" * 40)
                print(f"  {self.current_player.name} has won! ")
                print("=" * 40)
                break


            if self.board.is_full():
                self.board.display()
                print()
                print("=" * 40)
                print("  It is a tie! No more turns left.")
                print("=" * 40)
                break

            self.switch_player()
            print()