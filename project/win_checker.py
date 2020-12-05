from project.board import Board


class WinChecker:

    def player_one_wins(self, board: Board):
        row_win = ""
        col_win_one = ""
        col_win_two = ""
        col_win_three = ""
        right_diagonal_win = ""
        left_diagonal_win = ""
        #index counters for checking symbol on board
        col_count_right = -1
        col_count_left = 3

        for row_i, row in enumerate(board.board):

            col_count_right += 1
            col_count_left -= 1
            #checking if player has a diagonal left to right win
            if board.board[row_i][col_count_right] == "X":
                right_diagonal_win += "X"
                if right_diagonal_win == "XXX":
                    self.player_one_win = True
                    break
            #checking if player has a diagonal right to left win
            if board.board[row_i][col_count_left] == "X":
                left_diagonal_win += "X"
                if left_diagonal_win == "XXX":
                    self.player_one_win = True
                    break

            for col_i, col in enumerate(row):

                if col == "X":
                #adding X's to row_win to check if any of the rows win
                    row_win += "X"

                if row_win == "XXX":
                    self.player_one_win = True
                    break
                #if no three X's are found in a row , row_win will restart for next row
                if col_i == 2:
                    row_win = ""
                #adding X's to col_win and checking if any of the columns are winners
                if col_i == 0 and col == "X":
                    col_win_one += "X"
                elif col_i == 1 and col == "X":
                    col_win_two += "X"
                elif col_i == 2 and col == "X":
                    col_win_three += "X"
                if col_win_one == "XXX":
                    self.player_one_win = True
                elif col_win_two == "XXX":
                    self.player_one_win = True
                elif col_win_three == "XXX":
                    self.player_one_win = True


    def computer_wins(self, board: Board):
        row_win = ""
        col_win_one = ""
        col_win_two = ""
        col_win_three = ""
        right_diagonal_win = ""
        left_diagonal_win = ""
        #index counters for checking symbol on board
        col_count_right = -1
        col_count_left = 3

        for row_i, row in enumerate(board.board):

            col_count_right += 1
            col_count_left -= 1
            #checking if computer has a diagonal left to right win
            if board.board[row_i][col_count_right] == "O":
                right_diagonal_win += "O"
                if right_diagonal_win == "OOO":
                    self.player_two_win = True
                    break
            #checking if computer has a diagonal right to left win
            if board.board[row_i][col_count_left] == "O":
                left_diagonal_win += "O"
                if left_diagonal_win == "OOO":
                    self.player_two_win = True
                    break

            for col_i, col in enumerate(row):

                if col == "O":
                #adding O's to row_win to check if any of the rows win
                    row_win += "O"

                if row_win == "OOO":
                    self.player_two_win = True
                    break
                #if no three O's are found in a row , row_win will restart for next row
                if col_i == 2:
                    row_win = ""
                #adding O's to col_win and checking if any of the columns are winners
                if col_i == 0 and col == "O":
                    col_win_one += "O"
                elif col_i == 1 and col == "O":
                    col_win_two += "O"
                elif col_i == 2 and col == "O":
                    col_win_three += "O"
                if col_win_one == "OOO":
                    self.player_two_win = True
                elif col_win_two == "OOO":
                    self.player_two_win = True
                elif col_win_three == "OOO":
                    self.player_two_win = True
