class Board:
    """
    Represents the Connect Four game board.
    """

    def __init__(self):
        """
        Initializes an empty 6x7 game board.
        """
        self.grid = [ #Game Board Structure, 0 = empty field
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]


    def is_valid_move(self, column):
        """
        Checks whether a move in the given column is valid.
        """
        if column < 0 or column >= 7:
            return False

        if self.grid[0][column] != 0:
            return False

        return True
        

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
