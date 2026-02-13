import random

class Player:
    """
    Represents a human player in the Connect4 game.

    Stores the player's name and symbol
    and handles user input for moves.
    """
    def __init__(self, name, symbol):
            """
            Initializes a player.

            Args:
                name (str): The player's name.
                symbol (str): The symbol used on the board (e.g., 'X' or 'O').
            """
        self.name = name
        self.symbol = symbol

    def get_move(self, board) -> int:
            """
            Prompts the player to choose a column.

            The player can:
            - Enter a number between 1 and 7
            - Press 'Q' to quit the game

            Args:
                board (Board): The current game board.

            Returns:
                int: Column index (0-6) or -1 if the player quits.
            """
        while True:
            choice = input(f"{self.name}, choose a column from (1-7) or press Q to end your move: ")
            if choice == "q":
                return -1
            if choice.isdigit():
                zahl = int(choice)

                if zahl >= 1 and zahl <= 7:
                    return zahl - 1
            print("Invalid Move, please choose another number.")

class Computer(Player):
    def get_move(self, board) -> int:
            """
            Selects a random valid column.

            Args:
                board (Board): The current game board.

            Returns:
                int: A valid column index or -1 if no move is possible.
            """
        free =[]
        for i in range(7):
            if not board.is_full(i):
                free.append(i)
        if free:
            turn = random.choice(free)
            print(f"{self.name} chooses {turn + 1}")
            return turn

        return -1



