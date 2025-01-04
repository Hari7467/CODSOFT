import random

PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_X):
        return -10 + depth
    if check_winner(board, PLAYER_O):
        return 10 - depth
    if is_full(board):
        return 0

    if is_maximizing:
        best = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    best = max(best, minimax(board, depth + 1, False))
                    board[row][col] = EMPTY
        return best
    else:
        best = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    best = min(best, minimax(board, depth + 1, True))
                    board[row][col] = EMPTY
        return best

def best_move(board):
    best_val = -float('inf')
    move = (-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O
                move_val = minimax(board, 0, False)
                board[row][col] = EMPTY
                if move_val > best_val:
                    move = (row, col)
                    best_val = move_val

    return move

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                break
            else:
                print("That space is already taken!")
        except (ValueError, IndexError):
            print("Invalid move! Enter a number between 1 and 9.")

def play_game():
    board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
    print_board(board)

    while True:
        player_move(board)
        print_board(board)

        if check_winner(board, PLAYER_X):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        print("AI is making its move...")
        move = best_move(board)
        board[move[0]][move[1]] = PLAYER_O
        print_board(board)

        if check_winner(board, PLAYER_O):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
