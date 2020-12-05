class Board:

    board_full = False

    def __init__(self):
        self.__board = []
        for i in range(3):
            self.board.append(["."] * 3)
        self.board_full = False

    def print_board(self):
        #prints the board on the concole
        result = '  A   B   C\n'
        for num, row in enumerate(self.board):
            result += f"{num + 1} "
            result += f"{'   '.join(row)}\n"
            result += f"\n"
        return result

    def check_if_board_full(self):
        # ' . ' means that the space is free for player one or player two to place a symbol
        # this counts how many free spaces are left , stopping the game if the board is full
        dot_counter = 0
        for row in self.board:
            for symbol in row:
                if symbol == ".":
                    dot_counter += 1
        if dot_counter == 0:
            self.board_full = True

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, value):
        self.__board = value
