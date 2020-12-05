from project.win_checker import WinChecker


class PlayerOne(WinChecker):

    def __init__(self):
        self.player_one_win = False

    #this method converts the user input in to valid indexes that can be used on the board
    def convert_user_input(self, x, y):
        if x == '1':
            x = 0
        elif x == '2':
            x = 1
        elif x == '3':
            x = 2

        if y == "a":
            y = 0
        elif y == "b":
            y = 1
        elif y == "c":
            y = 2
        return x, y

    #this will mark the player's choosen possition if it meets the conditions
    def mark_x(self, board):

        rows = ['1', '2', '3']
        cols = ['a', 'b', 'c']

        while True:
            y = input("Enter column: \n").lower()
            x = input("Enter row: \n").lower()
            if x in rows and y in cols:
                x, y = self.convert_user_input(x, y)
                if board.board[x][y] == '.':
                    board.board[x][y] = "X"
                    break
                else:
                    print("You can only place 'X' on a free spot - ' . '\n")

            else:
                print('Enter a valid position!\n')
