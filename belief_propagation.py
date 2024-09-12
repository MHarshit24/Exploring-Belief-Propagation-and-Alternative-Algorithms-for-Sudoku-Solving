# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox
import numpy as np
import time

# Class for Sudoku Solver GUI
class SudokuSolverGUI:
    def __init__(self, master):
        # Initializing the GUI
        self.master = master
        self.master.title("Sudoku Solver")

        # Creating the grid frame
        self.grid_frame = tk.Frame(master)
        self.grid_frame.pack()

        # Creating Sudoku grid cells
        self.cells = [[None]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.cells[i][j] = tk.Entry(self.grid_frame, width=3, font=('Helvetica', 16))
                self.cells[i][j].grid(row=i, column=j)

        # Creating buttons for loading puzzles and solving
        self.load_default_button = tk.Button(master, text="Load Default Puzzle", command=self.load_default_puzzle)
        self.load_default_button.pack()
        self.load_easy_button = tk.Button(master, text="Load Easy Puzzle", command=self.load_easy_puzzle)
        self.load_easy_button.pack()
        self.load_medium_button = tk.Button(master, text="Load Medium Puzzle", command=self.load_medium_puzzle)
        self.load_medium_button.pack()
        self.load_hard_button = tk.Button(master, text="Load Hard Puzzle", command=self.load_hard_puzzle)
        self.load_hard_button.pack()

        self.solve_button = tk.Button(master, text="Solve", command=self.solve_sudoku)
        self.solve_button.pack()

    # Loading default puzzle
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

    # Loading easy puzzle
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

    # Loading medium puzzle
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

    # Loading hard puzzle
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

    # Loading puzzle into GUI
    def load_puzzle(self, puzzle):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                if puzzle[i][j] != 0:
                    self.cells[i][j].insert(0, puzzle[i][j])

    # Solving Sudoku puzzle
    def solve_sudoku(self):
        puzzle = np.zeros((9, 9))
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

        # Timing the solving process
        start_time = time.time()
        solved = self.solve(puzzle)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Displaying the solution or no solution message
        if solved is not None:
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].delete(0, tk.END)
                    self.cells[i][j].insert(0, int(solved[i][j]))
            messagebox.showinfo("Info", "Puzzle solved in {:.4f} seconds".format(elapsed_time))
        else:
            messagebox.showinfo("Info", "No solution found")

    # Propagating messages for belief propagation algorithm
    def propagate_messages(self, beliefs):
        messages = np.ones((9, 9, 9, 3)) / 9

        for i in range(9):
            for j in range(9):
                if np.any(beliefs[i, j] > 1e-10):
                    value = np.argmax(beliefs[i, j])
                    messages[i, j, :, :] = 0
                    messages[i, j, value, :] = 1
                else:
                    row_values = beliefs[i, :].copy()
                    row_values[j] = 0
                    col_values = beliefs[:, j].copy()
                    col_values[i] = 0
                    box_values = beliefs[(i // 3) * 3:(i // 3 + 1) * 3, (j // 3) * 3:(j // 3 + 1) * 3].flatten()
                    box_values[(i % 3) * 3 + (j % 3)] = 0

                    if row_values.sum() > 0:
                        row_values /= row_values.sum()
                    if col_values.sum() > 0:
                        col_values /= col_values.sum()
                    if box_values.sum() > 0:
                        box_values /= box_values.sum()

                    messages[i, j, :, 0] = row_values
                    messages[i, j, :, 1] = col_values
                    messages[i, j, :, 2] = box_values

        return messages

    # Updating beliefs in belief propagation algorithm
    def update_beliefs(self, beliefs, messages):
        updated_beliefs = beliefs.copy()

        for i in range(9):
            for j in range(9):
                if not np.any(np.isclose(beliefs[i, j], 0)):
                    continue

                belief_product = np.prod(messages[i, j], axis=1)
                updated_beliefs[i, j] *= belief_product

                if np.sum(updated_beliefs[i, j]) > 0:
                    updated_beliefs[i, j] /= np.sum(updated_beliefs[i, j])

        return updated_beliefs

    # Solving Sudoku puzzle using belief propagation or backtracking
    def solve(self, puzzle):
        beliefs = np.ones((9, 9, 9))
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != 0:
                    beliefs[i, j, :] = 0
                    beliefs[i, j, int(puzzle[i][j]) - 1] = 1

        for _ in range(10):  # Limit iterations to avoid infinite loop
            messages = self.propagate_messages(beliefs)
            beliefs = self.update_beliefs(beliefs, messages)
            if np.all(np.sum(beliefs, axis=2) == 1):
                break

        if np.any(np.sum(beliefs, axis=2) != 1):
            # Belief propagation did not converge to a solution, use backtracking
            solution = self.backtrack(puzzle, beliefs)
            return solution
        else:
            solution = np.argmax(beliefs, axis=2) + 1
            return solution

    # Checking if a number is valid in a Sudoku puzzle
    def is_valid(self, puzzle, row, col, num):
        for i in range(9):
            if puzzle[row][i] == num or puzzle[i][col] == num:
                return False
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if puzzle[i][j] == num:
                    return False
        return True

    # Backtracking algorithm to solve Sudoku puzzle
    def backtrack(self, puzzle, beliefs):
        empty_cells = [(i, j) for i in range(9) for j in range(9) if puzzle[i][j] == 0]

        def backtrack_solve(index):
            if index == len(empty_cells):
                return True

            i, j = empty_cells[index]
            probabilities = beliefs[i, j]
            numbers = np.argsort(probabilities)[::-1] + 1  # Sort numbers by their probabilities

            for num in numbers:
                if self.is_valid(puzzle, i, j, num):
                    puzzle[i][j] = num
                    if backtrack_solve(index + 1):
                        return True
                    puzzle[i][j] = 0

            return False

        if backtrack_solve(0):
            return puzzle
        else:
            return None

def main():
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()