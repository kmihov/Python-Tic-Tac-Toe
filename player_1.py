from TicTacToe.win_checker import WinChecker


class PlayerOne(WinChecker):

    def __init__(self):
        self.player_one_win = False

    @staticmethod
    def mark_x(board, y, x):
        try:
            if x == '1':
                x = 0
            elif x == '2':
                x = 1
            elif x == '3':
                x = 2
        except TabError:
            return "Enter a valid column"

        try:
            if y =="a":
                y = 0
            elif y == "b":
                y = 1
            elif y == "c":
                y = 2
        except TabError:
            return "Enter a valid row"

        board.board[x][y] = "X"
