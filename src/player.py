import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self, board) -> int:
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
        free =[]
        for i in range(7):
            if not board.is_full(i):
                free.append(i)
        if free:
            turn = random.choice(free)
            print(f"{self.name} chooses {turn + 1}")
            return turn

        return -1



