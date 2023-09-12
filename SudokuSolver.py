import random

def generate_board():
    board = [['-' for _ in range(9)] for _ in range(9)]
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    
    # Place 4 random numbers in different positions
    for num in numbers[:4]:
        while True:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if board[row][col] == '-' and is_valid_move(board, row, col, num):
                board[row][col] = str(num)
                break
    
    return board


def solve_sudoku(board):
    if is_board_full(board):
        return True

    row, col = find_empty_cell(board)
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = str(num)
            if solve_sudoku(board):
                return True
            board[row][col] = '-'

    return False


def is_board_full(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '-':
                return False
    return True


def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '-':
                return row, col
    return None, None


def is_valid_move(board, row, col, num):
    # Check if the number is already present in the row
    for i in range(9):
        if board[row][i] == str(num):
            return False

    # Check if the number is already present in the column
    for i in range(9):
        if board[i][col] == str(num):
            return False

    # Check if the number is already present in the 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == str(num):
                return False

    return True


def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print('---------------------')
        for j, cell in enumerate(row):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            print(cell, end=' ')
        print()


# Example board generation
board = generate_board()

print("Initial Sudoku board:")
print_board(board)
print("------------------------")
solve_sudoku(board)

print("\nFinal Sudoku board:")
print_board(board)
