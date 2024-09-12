import tkinter as tk
from tkinter import messagebox
import time

class SudokuSolverGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")

        # Create a frame to hold the Sudoku grid
        self.grid_frame = tk.Frame(master)
        self.grid_frame.pack()

        # Create a 9x9 grid of Entry widgets to represent the Sudoku puzzle
        self.cells = [[None]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.cells[i][j] = tk.Entry(self.grid_frame, width=3, font=('Helvetica', 16))
                self.cells[i][j].grid(row=i, column=j)

        # Load buttons to load different predefined puzzles
        self.load_default_button = tk.Button(master, text="Load Default Puzzle", command=self.load_default_puzzle)
        self.load_default_button.pack()
        self.load_easy_button = tk.Button(master, text="Load Easy Puzzle", command=self.load_easy_puzzle)
        self.load_easy_button.pack()
        self.load_medium_button = tk.Button(master, text="Load Medium Puzzle", command=self.load_medium_puzzle)
        self.load_medium_button.pack()
        self.load_hard_button = tk.Button(master, text="Load Hard Puzzle", command=self.load_hard_puzzle)
        self.load_hard_button.pack()

        # Create a "Solve" button to initiate the solving process
        self.solve_button = tk.Button(master, text="Solve", command=self.solve_sudoku)
        self.solve_button.pack()

    # Function to load the default Sudoku puzzle
    def load_default_puzzle(self):
        puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.load_puzzle(puzzle)

    # Function to load an easy Sudoku puzzle
    def load_easy_puzzle(self):
        puzzle = [
            [6, 7, 2, 0, 0, 3, 0, 0, 4],
            [0, 3, 1, 0, 0, 0, 2, 5, 0],
            [0, 4, 0, 0, 0, 0, 0, 1, 3],
            [1, 0, 7, 0, 4, 0, 0, 0, 0],
            [3, 9, 0, 0, 0, 0, 0, 4, 5],
            [2, 0, 0, 0, 7, 5, 1, 0, 6],
            [0, 0, 5, 0, 9, 6, 3, 7, 8],
            [0, 6, 0, 5, 0, 8, 0, 0, 9],
            [9, 0, 0, 0, 0, 7, 5, 0, 1]
        ]
        self.load_puzzle(puzzle)

    # Function to load a medium Sudoku puzzle
    def load_medium_puzzle(self):
        puzzle = [
            [0, 3, 2, 0, 4, 0, 0, 0, 0],
            [4, 1, 0, 0, 0, 0, 0, 2, 6],
            [0, 0, 0, 9, 0, 0, 3, 0, 0],
            [0, 0, 0, 8, 6, 0, 2, 0, 5],
            [1, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 8, 4, 0, 0, 0, 3, 9],
            [6, 0, 0, 0, 9, 5, 0, 0, 0],
            [9, 8, 1, 0, 7, 3, 4, 0, 2],
            [0, 2, 5, 0, 8, 4, 6, 9, 7]
        ]
        self.load_puzzle(puzzle)

    # Function to load a hard Sudoku puzzle
    def load_hard_puzzle(self):
        puzzle = [
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 0, 7, 0, 1, 0],
            [7, 6, 0, 9, 0, 0, 3, 0, 8],
            [0, 0, 1, 6, 0, 0, 4, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 5, 0, 0, 7, 0, 0, 8, 0],
            [0, 0, 3, 0, 0, 1, 0, 2, 0],
            [9, 1, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 0, 0, 5, 1, 9, 0]
        ]
        self.load_puzzle(puzzle)

    # Function to load a puzzle into the Sudoku grid
    def load_puzzle(self, puzzle):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                if puzzle[i][j] != 0:
                    self.cells[i][j].insert(0, puzzle[i][j])

    # Function to solve the Sudoku puzzle
    def solve_sudoku(self):
        # Extract the Sudoku puzzle from the grid
        puzzle = [[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                try:
                    value = self.cells[i][j].get().strip()
                    if value:
                        value = int(value)
                        if value < 1 or value > 9:
                            raise ValueError
                        puzzle[i][j] = value
                except ValueError:
                    messagebox.showerror("Error", "Invalid input in cell ({}, {})".format(i+1, j+1))
                    return
        
        # Solve the Sudoku puzzle
        start_time = time.time()  # Start timing
        self.iteration_count = 0  # Initialize iteration count
        if self.solve(puzzle):
            end_time = time.time()  # End timing
            total_time = end_time - start_time  # Calculate the time taken
            messagebox.showinfo("Info", f"Sudoku Solved!\nTime taken: {total_time:.2f} seconds\nIterations: {self.iteration_count}")
        else:
            messagebox.showinfo("Info", "No solution found")

    # Recursive function to solve the Sudoku puzzle
    def solve(self, puzzle):
        self.iteration_count += 1  # Increment iteration count
        # Find the next empty cell in the puzzle
        empty_cell = self.find_empty_cell(puzzle)
        if not empty_cell:
            return True  # Puzzle solved
        
        row, col = empty_cell
        for num in range(1, 10):
            # Check if placing num in the empty cell is valid
            if self.is_valid_move(puzzle, row, col, num):
                puzzle[row][col] = num
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, num)
                self.cells[row][col].update_idletasks()
                # Recursively solve the updated puzzle
                if self.solve(puzzle):
                    return True
                # Backtrack if no solution found
                puzzle[row][col] = 0
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, "")
                self.cells[row][col].update_idletasks()
        return False

    # Function to find the next empty cell in the Sudoku puzzle
    def find_empty_cell(self, puzzle):
        # Find the next empty cell in the puzzle
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    return (i, j)
        return None

    # Function to check if a move is valid in the Sudoku puzzle
    def is_valid_move(self, puzzle, row, col, num):
        # Check if placing num in the given cell is valid
        # Check row
        if num in puzzle[row]:
            return False

        # Check column
        if num in [puzzle[i][col] for i in range(9)]:
            return False

        # Check subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if puzzle[i][j] == num:
                    return False
        return True

def main():
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()