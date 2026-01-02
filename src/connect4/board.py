class Board:
    """
    Represents the Connect Four game board.
    """

    def __init__(self):
        """
        Initializes an empty 6x7 game board.
        """
        self.grid = []

    def is_valid_move(self, column):
        """
        Checks whether a move in the given column is valid.
        """
        pass

    def drop_stone(self, column, player):
        """
        Drops a stone into the given column for the given player.
        """
        pass

    def check_win(self, player):
        """
        Checks whether the given player has won the game.
        """
        pass
