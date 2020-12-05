from TicTacToe.board import Board
from TicTacToe.player_1 import PlayerOne
from TicTacToe.player_2 import PlayerTwo


def check_if_player_one_wins(player: PlayerOne, board):
    player.player_one_wins(board)
    if player.player_one_win:
        global user_wins
        user_wins += 1
        print(f"YOU WIN!\nYour wins:{user_wins} form {game_counter} games played.")
        return True


def check_if_player_two_wins(player: PlayerTwo, board):
    player.computer_wins(board)
    if player.player_two_win:
        global computer_wins
        computer_wins += 1
        print(f"Computer won!\nComputer wins: {computer_wins}\nYour wins:{user_wins}\nfrom {game_counter} games played")
        return True


def check_if_playfield_is_full(board: Board):
    board.check_if_board_full()
    if board.board_full:
        global draws
        draws += 1
        print(f"DRAW!\nDraws: {draws}\nYour wins:{user_wins}\nComputer wins: {computer_wins}\nfrom {game_counter} games played")
        return True


game_counter = 0
user_wins = 0
computer_wins = 0
draws = 0
cols = ('a', 'b', 'c')
rows = (1, 2, 3)

while True:
    game_counter += 1

    start_end_game = input("Start new game? - Yes, - No\n").lower()
    if start_end_game == "no":
        break
    elif start_end_game == "yes":
        b = Board()
        p_one = PlayerOne()
        p_two = PlayerTwo()
        print(b.print_board())

        while True:

            if game_counter % 2 == 1:
                col = input("Enter column: \n").lower()
                row = input("Enter row: \n").lower()

                #if cols not in cols or rows not in rows:
                    #while True:
                        #print("Please enter a valid column and row.\n")
                        #col = input("Enter column: \n").lower()
                        #row = input("Enter row: \n").lower()
                        #if col in cols:
                            #if row in rows:
                                #break

                print(p_one.mark_x(b, col, row))
                print(b.print_board())

                check = check_if_player_one_wins(p_one, b)
                if check:
                    break

                check = check_if_playfield_is_full(b)
                if check:
                    break

                #player two turn
                p_two.first_turn += 1
                p_two.play_to_win(b)

                if p_two.has_played:
                    p_two.has_played = False
                    print(b.print_board())
                    check = check_if_player_two_wins(p_two, b)
                    if check:
                        break
                    continue

                p_two.block(b)
                if p_two.has_played:
                    p_two.has_played = False
                    print(b.print_board())
                    check = check_if_player_two_wins(p_two, b)
                    if check:
                        break
                    continue

                p_two.play_on_free_spot_wen_no_winning_moves(b)
                if p_two.has_played:
                    p_two.has_played = False
                    print(b.print_board())
                    check = check_if_player_two_wins(p_two, b)
                    if check:
                        break
                    continue

                check = check_if_playfield_is_full(b)
                if check:
                    break

            elif game_counter % 2 == 0:

                # player two starts the game
                p_two.play_to_win(b)
                if p_two.has_played:
                    p_two.has_played = False
                    p_two.first_turn += 1
                    print(b.print_board())

                    check = check_if_player_two_wins(p_two, b)
                    if check:
                        break
                    check = check_if_player_one_wins(p_one, b)
                    if check:
                        break

                    check = check_if_playfield_is_full(b)
                    if check:
                        break

                    p_one.mark_x(b, input("enter column: \n").lower(), input("enter row: \n"))
                    print(b.print_board())
                    continue


                p_two.block(b)
                if p_two.has_played:
                    p_two.has_played = False
                    p_two.first_turn += 1
                    print(b.print_board())

                    check = check_if_player_two_wins(p_two, b)
                    if check:
                        break
                    check = check_if_player_one_wins(p_one, b)
                    if check:
                        break

                    check = check_if_playfield_is_full(b)
                    if check:
                        break

                    p_one.mark_x(b, input("enter column: \n").lower(), input("enter row: \n"))
                    print(b.print_board())
                    continue


                p_two.play_on_free_spot_wen_no_winning_moves(b)
                if p_two.has_played:
                    p_two.has_played = False
                    p_two.first_turn += 1
                    print(b.print_board())

                    check = check_if_player_two_wins(p_two, b)
                    if check:
                        break
                    check = check_if_player_one_wins(p_one, b)
                    if check:
                        break
                    check = check_if_playfield_is_full(b)
                    if check:
                        break

                    p_one.mark_x(b, input("enter column: \n").lower(), input("enter row: \n"))
                    print(b.print_board())
                    continue

#apply difficulty level
#check bug : BOARD IS FULL AND GAME END! YET ASKS FOR INPUT..?
#