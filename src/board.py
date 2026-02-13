class Board:
        """
        Represents the Connect4 game board.
        Handles the grid and game logic related to the board.
        """
    def __init__(self):
            """
            Initializes the Connect4 board.

            Creates a 6x7 grid filled with 0.
            0 represents an empty field.
            """
        self.grid = [ #Game Board Structure, 0 = empty field
        [0, 0, 0, 0, 0, 0, 0], #First Row from Above
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]


    def is_valid_move(self, column):
            """
            Checks if a move in the given column is valid.

            Args:
                column (int): The column number (0-6).

            Returns:
                bool: True if the move is valid, False otherwise.
            """
        if column < 0 or column >= 7:
            return False

        if self.grid[0][column] != 0:
            return False

        return True


    def drop_stone(self, column, player):
            """
            Drops a player's stone into the selected column.

            The stone will be placed in the lowest empty row.

            Args:
                column (int): The column where the stone is dropped.
                player (int or str): The player identifier.

            Returns:
                bool: True if the stone was placed successfully.
            """
        for row in range(5, -1, -1): #Checks if field is empty
            if self.grid[row][column] == 0:
                self.grid[row][column] = player
                return True

    def is_full(self, col = None):
            """
            Checks if the board or a specific column is full.

            Args:
                col (int, optional): Column index to check. 
                                     If None, checks if the entire board is full.

            Returns:
                bool: True if full, False otherwise.
            """
        if col is not None:
            return self.grid[0][col] != 0
        return all(self.grid[0][col] != 0 for col in range(7))


    def check_win(self, player):
            """
            Checks if the given player has won the game.

            A win occurs when the player has four consecutive stones
            horizontally, vertically, or diagonally.

            Args:
                player (int or str): The player identifier.

            Returns:
                bool: True if the player has won, False otherwise.
            """
        for row in range(6):
            for col in range(4):
                if (
                        self.grid[row][col] == player and
                        self.grid[row][col + 1] == player and
                        self.grid[row][col + 2] == player and
                        self.grid[row][col + 3] == player
                ):
                    return True

            #Vertical
        for row in range(3):
            for col in range(7):
                if (
                        self.grid[row][col] == player and
                        self.grid[row + 1][col] == player and
                        self.grid[row + 2][col] == player and
                        self.grid[row + 3][col] == player
                ):
                    return True

            # Diagonal down-right
        for row in range(3):
            for col in range(4):
                if (
                        self.grid[row][col] == player and
                        self.grid[row + 1][col + 1] == player and
                        self.grid[row + 2][col + 2] == player and
                        self.grid[row + 3][col + 3] == player
                ):
                    return True

            # Diagonal down-left
        for row in range(3):
            for col in range(3, 7):
                if (
                        self.grid[row][col] == player and
                        self.grid[row + 1][col - 1] == player and
                        self.grid[row + 2][col - 2] == player and
                        self.grid[row + 3][col - 3] == player
                    ):
                    return True

        return False

    def display(self):
            """
            Prints the current board state to the console.

            Shows column numbers and visualizes the grid.
            Empty cells (0) are displayed as '.' for readability.

            Returns:
                None
            """
        print("\n  1 2 3 4 5 6 7")  # Column numbers for the player
        print("---------------")
        for row in self.grid:
            # This joins the numbers in the row with a pipe | symbol
            # and replaces 0 with a dot . to make it look nicer
            row_str = " ".join([str(cell) if cell != 0 else "." for cell in row])
            print(f"| {row_str} |")
        print("---------------\n")
