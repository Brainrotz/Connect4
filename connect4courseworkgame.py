def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def initialize_board():
    return [['.' for _ in range(7)] for _ in range(6)]

def valid_spot(board, column):
    return 0 <= column < 7 and board[0][column] == '.'

def drop_piece(board, column, player):
    for row in range(5, -1, -1):
        if board[row][column] == '.':
            board[row][column] = player
            return True
    return False

def check_win(board, player):
    # Check horizontal collum
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertical collum
    for col in range(7):
        for row in range(3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonals collum
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
            if all(board[row + i][col + 3 - i] == player for i in range(4)):
                return True

    return False

def play_connect4():
    board = initialize_board()
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        column = int(input(f"Player {players[turn]}, choose a column (0-6): "))

        if valid_spot(board, column):
            drop_piece(board, column, players[turn])

            if check_win(board, players[turn]):
                print_board(board)
                print(f"Player {players[turn]} wins! Thanks for playing")
                break

            if all(cell != '.' for row in board for cell in row):
                print_board(board)
                print("It's a tie!")
                break

            turn = 1 - turn
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_connect4()
