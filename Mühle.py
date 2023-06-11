import random

def print_board(board):
    print("     {}   {}   {}".format(board[0], board[1], board[2]))
    print("    ---+---+---")
    print(" {}  {}   {}  {}".format(board[3], board[4], board[5], board[6]))
    print("    ---+---+---")
    print("     {}   {}   {}".format(board[7], board[8], board[9]))

def check_win(board, player):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontale Reihen
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertikale Reihen
        [1, 5, 9], [3, 5, 7]  # Diagonale Reihen
    ]
    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

def get_empty_positions(board):
    return [pos for pos in range(1, 10) if board[pos] == ' ']

def make_move(board, position, player):
    board[position] = player

def cpu_move(board, player):
    empty_positions = get_empty_positions(board)
    return random.choice(empty_positions)

def play_muehle():
    board = [' '] * 10
    players = ['X', 'O']
    current_player = random.choice(players)

    while True:
        print_board(board)

        if len(get_empty_positions(board)) == 0:
            print("Das Spiel endet unentschieden!")
            break

        if current_player == 'X':
            position = int(input("Wähle eine Position (1-9): "))
            if board[position] != ' ':
                print("Ungültige Position. Versuche es erneut.")
                continue
        else:
            position = cpu_move(board, current_player)

        make_move(board, position, current_player)

        if check_win(board, current_player):
            print_board(board)
            print("Spieler {} hat Gewonnen!!!!".format(current_player))
            break

        current_player = players[1 - players.index(current_player)]  # Wechsel Spieler

play_muehle()
