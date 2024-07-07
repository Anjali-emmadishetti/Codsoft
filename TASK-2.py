import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_moves_left(board):
    for row in board:
        if "_" in row:
            return True
    return False

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "_":
            return 10 if row[0] == 'X' else -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return 10 if board[0][col] == 'X' else -10

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return 10 if board[0][0] == 'X' else -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return 10 if board[0][2] == 'X' else -10

    return 0

def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_maximizing, alpha, beta))
                    board[i][j] = "_"
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_maximizing, alpha, beta))
                    board[i][j] = "_"
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = "_"
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def main():
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]

    while True:
        print_board(board)

        if not is_moves_left(board):
            print("It's a draw!")
            break

        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] != "_":
            print("Invalid move! Try again.")
            continue

        board[row][col] = 'O'

        if evaluate(board) == -10:
            print_board(board)
            print("You win!")
            break

        if not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'

        if evaluate(board) == 10:
            print_board(board)
            print("AI wins!")
            break

if __name__ == "__main__":
    main()
