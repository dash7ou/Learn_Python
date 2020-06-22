# -------- Global Varibles ------------#
board = []
player = 'X'
winner = None


def display_board():
    lines = []
    line = ''
    for index, _ in enumerate(board):
        if index in [2, 5, 8]:
            line = line + board[index]
            lines.append(line)
            line = ''
        else:
            line = line + board[index] + " | "

    for line in lines:
        print(line)


def change_player():
    global player
    player = "O" if player == "X" else "X"


def check_rows():
    if board[1] == board[2] == board[0]:
        return board[0]
    elif board[3] == board[4] == board[5]:
        return board[5]
    elif board[6] == board[7] == board[8]:
        return board[6]
    else:
        return None


def check_clumns():
    if board[3] == board[6] == board[0]:
        return board[0]
    elif board[1] == board[4] == board[7]:
        return board[1]
    elif board[2] == board[5] == board[8]:
        return board[2]
    else:
        return None


def check_diagonals():
    if board[4] == board[8] == board[0]:
        return board[0]
    elif board[2] == board[4] == board[6]:
        return board[2]
    else:
        return None


def handle_turn():
    position = input(
        'Choose a position from 1-9 (Enter > exit < to go out of game): ')
    if position == "exit":
        raise Exception('Exit')

    try:
        position = int(position) - 1
    except:
        raise Exception("String")

    if position not in range(0, 9):
        raise Exception("another number")

    if board[position] == '-':
        board[position] = player
        change_player()
    else:
        print('\n ####### choose another place :) ######## \n')


def check_winner():
    global winner
    row = check_rows()
    if row == "X" or row == "O":
        winner = row
        return
    else:
        clumn = check_clumns()
        if clumn == "X" or row == "O":
            winner = clumn
            return
        else:
            diagonal = check_diagonals()
            if diagonal == "X" or row == "O":
                winner = diagonal
                return


def start_game():
    global winner
    for _ in range(9):
        board.append("-")
    while "-" in board:
        display_board()
        try:
            handle_turn()
            check_winner()
            if winner is not None:
                print(f" >>>>>>> Winner is {winner} <<<<<<<")
                display_board()
                break
        except Exception as error:
            if error.args[0] == 'Exit':
                break
            else:
                print("\n >>>>> Enter invalid input <<<<<< \n")
                continue

    if winner is None:
        display_board()
        print("Game Over :-p")


start_game()
