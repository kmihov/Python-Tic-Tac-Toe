from TicTacToe.win_checker import WinChecker
from TicTacToe.board import Board
from random import randint

class PlayerTwo(WinChecker):
    first_turn = 0

    def __init__(self):
        self.player_two_win = False
        self.has_played = False

    def block(self, board:Board):
        for row_i, row in enumerate(board.board):
            r = ''.join(row)
            if r == 'X.X' or r == 'XX.' or r == '.XX':
                space_to_block_index = row.index('.')
                row[space_to_block_index] = "O"
                self.has_played = True
                break

        block_col_one = [board.board[0][0] + board.board[1][0] + board.board[2][0]]
        block_col_two = [board.board[0][1] + board.board[1][1] + board.board[2][1]]
        block_col_three = [board.board[0][2] + board.board[1][2] + board.board[2][2]]
        block_diagonal_right = [board.board[0][0] + board.board[1][1] + board.board[2][2]]
        block_diagonal_left = [board.board[0][2] + board.board[1][1] + board.board[2][0]]

        if not self.has_played:
            if 'XX.' in block_col_one:
                board.board[2][0] = 'O'
                self.has_played = True
            elif 'X.X' in block_col_one:
                board.board[1][0] = 'O'
                self.has_played = True
            elif '.XX' in block_col_one:
                board.board[0][0] = 'O'
                self.has_played = True

            elif 'XX.' in block_col_two:
                board.board[2][1] = 'O'
                self.has_played = True
            elif 'X.X' in block_col_two:
                board.board[1][1] = 'O'
                self.has_played = True
            elif '.XX' in block_col_two:
                board.board[0][1] = 'O'
                self.has_played = True

            elif 'XX.' in block_col_three:
                board.board[2][2] = 'O'
                self.has_played = True
            elif 'X.X' in block_col_three:
                board.board[1][2] = 'O'
                self.has_played = True
            elif '.XX' in block_col_three:
                board.board[0][2] = 'O'
                self.has_played = True

            elif 'XX.' in block_diagonal_right:
                board.board[2][2] = 'O'
                self.has_played = True
            elif 'X.X' in block_diagonal_right:
                board.board[1][1] = 'O'
                self.has_played = True
            elif '.XX' in block_diagonal_right:
                board.board[0][0] = 'O'
                self.has_played = True

            elif 'XX.' in block_diagonal_left:
                board.board[2][0] = 'O'
                self.has_played = True
            elif 'X.X' in block_diagonal_left:
                board.board[1][1] = 'O'
                self.has_played = True
            elif '.XX' in block_diagonal_left:
                board.board[0][2] = 'O'
                self.has_played = True

    def play_to_win(self, board:Board):

        if self.first_turn == 1:
            xy_position = None
            for i, row in enumerate(board.board):
                if 'X' in row:
                    xy_position = i, row.index('X')
                    break
            #this allows the computer to place 'O' at random the first turn it plays

            for _ in range(100):
                x, y = randint(0,2), randint(0,2)
                if x != xy_position[0] or y != xy_position[1]:
                    board.board[x][y] = 'O'
                    self.has_played = True
                    break

        elif self.first_turn == 0:
            x, y = randint(0, 2), randint(0, 2)
            board.board[x][y] = 'O'
            self.has_played = True

        elif self.first_turn > 1:
            for row_i, row in enumerate(board.board):
                r = ''.join(row)
                if r == 'O.O' or r == 'OO.' or r == '.OO':
                    space_index = row.index('.')
                    row[space_index] = "O"
                    self.has_played = True
                    break
            #getting all possible combinations on board to check AI win
            col_one = [board.board[0][0] + board.board[1][0] + board.board[2][0]]
            col_two = [board.board[0][1] + board.board[1][1] + board.board[2][1]]
            col_three = [board.board[0][2] + board.board[1][2] + board.board[2][2]]
            diagonal_right = [board.board[0][0] + board.board[1][1] + board.board[2][2]]
            diagonal_left = [board.board[0][2] + board.board[1][1] + board.board[2][0]]
            #this is where we check for a possible win
            if 'OO.' in col_one:
                board.board[2][0] = 'O'
                self.has_played = True
            elif 'O.O' in col_one:
                board.board[1][0] = 'O'
                self.has_played = True
            elif '.OO' in col_one:
                board.board[0][0] = 'O'
                self.has_played = True

            elif 'OO.' in col_two:
                board.board[2][1] = 'O'
                self.has_played = True
            elif 'O.O' in col_two:
                board.board[1][1] = 'O'
                self.has_played = True
            elif '.OO' in col_two:
                board.board[0][1] = 'O'
                self.has_played = True

            elif 'OO.' in col_three:
                board.board[2][2] = 'O'
                self.has_played = True
            elif 'O.O' in col_three:
                board.board[1][2] = 'O'
                self.has_played = True
            elif '.OO' in col_three:
                board.board[0][2] = 'O'
                self.has_played = True

            elif 'OO.' in diagonal_right:
                board.board[2][2] = 'O'
                self.has_played = True
            elif 'O.O' in diagonal_right:
                board.board[1][1] = 'O'
                self.has_played = True
            elif '.OO' in diagonal_right:
                board.board[0][0] = 'O'
                self.has_played = True

            elif 'OO.' in diagonal_left:
                board.board[2][0] = 'O'
                self.has_played = True
            elif 'O.O' in diagonal_left:
                board.board[1][1] = 'O'
                self.has_played = True
            elif '.OO' in diagonal_left:
                board.board[0][2] = 'O'
                self.has_played = True

        elif self.first_turn > 1:
            for row_i, row in enumerate(board.board):
                r = ''.join(row)
                if r == '..O' or r == 'O..' or r == '.O.':
                    space_index = row.index('.')
                    row[space_index] = "O"
                    self.has_played = True
                    break
            #getting all possible combinations on board to check AI win
            col_one = [board.board[0][0] + board.board[1][0] + board.board[2][0]]
            col_two = [board.board[0][1] + board.board[1][1] + board.board[2][1]]
            col_three = [board.board[0][2] + board.board[1][2] + board.board[2][2]]
            diagonal_right = [board.board[0][0] + board.board[1][1] + board.board[2][2]]
            diagonal_left = [board.board[0][2] + board.board[1][1] + board.board[2][0]]
            #this is where we check for a possible win
            if 'O..' in col_one:
                board.board[2][2] = 'O'
                self.has_played = True
            elif '..O' in col_one:
                board.board[0][0] = 'O'
                self.has_played = True
            elif '.O.' in col_one:
                board.board[2][0] = 'O'
                self.has_played = True

            elif 'O..' in col_two:
                board.board[2][2] = 'O'
                self.has_played = True
            elif '..O' in col_two:
                board.board[1][1] = 'O'
                self.has_played = True
            elif '.O.' in col_two:
                board.board[0][2] = 'O'
                self.has_played = True

            elif 'O..' in col_three:
                board.board[2][2] = 'O'
                self.has_played = True
            elif '..O' in col_three:
                board.board[0][2] = 'O'
                self.has_played = True
            elif '.O.' in col_three:
                board.board[0][2] = 'O'
                self.has_played = True

            elif 'O..' in diagonal_right:
                board.board[2][2] = 'O'
                self.has_played = True
            elif '..O' in diagonal_right:
                board.board[1][1] = 'O'
                self.has_played = True
            elif '.O.' in diagonal_right:
                board.board[0][0] = 'O'
                self.has_played = True

            elif 'O..' in diagonal_left:
                board.board[2][0] = 'O'
                self.has_played = True
            elif '..O' in diagonal_left:
                board.board[1][1] = 'O'
                self.has_played = True
            elif '.O.' in diagonal_left:
                board.board[0][2] = 'O'
                self.has_played = True

    def play_on_free_spot_wen_no_winning_moves(self, board: Board):
        symbol_placed = False
        if not self.has_played:
            for row_i, row in enumerate(board.board):
                for el_i, el in enumerate(row):
                    if el == '.':
                        board.board[row_i][el_i] = 'O'
                        symbol_placed = True
                        break
                if symbol_placed:
                    break
            self.has_played = True
