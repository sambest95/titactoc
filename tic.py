board = [["" for i_ in range(3)] for _ in range (3)]

def print_board(board):
    for row in board:
        print(" | " .join(row))
        print("-" *6)

print_board(board)