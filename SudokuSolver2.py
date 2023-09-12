import tkinter as tk
from tkinter import messagebox

def solve_sudoku(board):
    # Encontra uma célula vazia para começar a preencher
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # O tabuleiro está preenchido, a solução está encontrada

    row, col = empty_cell

    # Tenta preencher a célula vazia com um número válido
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # Solução encontrada

            board[row][col] = 0  # Volta atrás se não levar à solução

    return False  # Não foi possível encontrar uma solução

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board, row, col, num):
    # Verifica se o número é válido na linha e coluna
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Verifica se o número é válido no bloco 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_button_clicked():
    board = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if entry_boxes[i][j].get().isdigit():
                board[i][j] = int(entry_boxes[i][j].get())
    
    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entry_boxes[i][j].delete(0, tk.END)
                entry_boxes[i][j].insert(0, str(board[i][j]))
    else:
        messagebox.showinfo("Sem Solução", "Não foi possível encontrar uma solução para o Sudoku.")

# Criação da interface gráfica
root = tk.Tk()
root.title("Solver de Sudoku")

entry_boxes = [[None] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        entry_boxes[i][j] = tk.Entry(root, width=3, font=("Helvetica", 24))
        entry_boxes[i][j].grid(row=i, column=j)

solve_button = tk.Button(root, text="Resolver", command=solve_button_clicked)
solve_button.grid(row=9, columnspan=9)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

def solve_sudoku(board):
    # Encontra uma célula vazia para começar a preencher
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # O tabuleiro está preenchido, a solução está encontrada

    row, col = empty_cell

    # Tenta preencher a célula vazia com um número válido
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # Solução encontrada

            board[row][col] = 0  # Volta atrás se não levar à solução

    return False  # Não foi possível encontrar uma solução

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board, row, col, num):
    # Verifica se o número é válido na linha e coluna
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Verifica se o número é válido no bloco 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_button_clicked():
    board = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if entry_boxes[i][j].get().isdigit():
                board[i][j] = int(entry_boxes[i][j].get())
    
    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entry_boxes[i][j].delete(0, tk.END)
                entry_boxes[i][j].insert(0, str(board[i][j]))
    else:
        messagebox.showinfo("Sem Solução", "Não foi possível encontrar uma solução para o Sudoku.")

# Criação da interface gráfica
root = tk.Tk()
root.title("Solver de Sudoku")

entry_boxes = [[None] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        entry_boxes[i][j] = tk.Entry(root, width=3, font=("Helvetica", 24))
        entry_boxes[i][j].grid(row=i, column=j)

solve_button = tk.Button(root, text="Resolver", command=solve_button_clicked)
solve_button.grid(row=9, columnspan=9)

root.mainloop()
