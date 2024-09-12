# Importing the time module for timing the solving process
import time

class SudokuSolver:
    def __init__(self, puzzle):
        # Initializing the SudokuSolver object with the given puzzle
        self.grid = puzzle
        # Initializing the possibilities matrix based on the given puzzle
        self.possibilities = self.initialize_possibilities()

    def initialize_possibilities(self):
        # Initializing a matrix representing the possibilities for each cell
        possibilities = [[[1]*9 for _ in range(9)] for _ in range(9)]  # All possibilities initially allowed
        # Iterating through the puzzle to update possibilities based on initial values
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    # If a cell has a fixed value, update its possibilities accordingly
                    possibilities[i][j] = [0]*9
                    possibilities[i][j][self.grid[i][j] - 1] = 1
        return possibilities

    def propagate_constraints(self):
        # Propagating constraints based on current grid state
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:  # If cell is empty
                    # For each empty cell, check row, column, and box constraints
                    for num in range(1, 10):
                        if num in self.get_row(i) or num in self.get_col(j) or num in self.get_box(i, j):
                            # If a number is found in row, column, or box, it's not a possibility
                            self.possibilities[i][j][num - 1] = 0

    def get_row(self, i):
        # Get the values in the specified row
        return [self.grid[i][j] for j in range(9)]

    def get_col(self, j):
        # Get the values in the specified column
        return [self.grid[i][j] for i in range(9)]

    def get_box(self, i, j):
        # Get the values in the box containing the specified cell
        box_i, box_j = (i // 3) * 3, (j // 3) * 3
        return [self.grid[box_i + x][box_j + y] for x in range(3) for y in range(3)]

    def is_solved(self):
        # Check if the Sudoku grid is completely filled
        return all(0 not in row for row in self.grid)

    def solve(self):
        # Solving the Sudoku puzzle
        start_time = time.time()  # Start timing
        unsolved_sudoku = [[self.grid[i][j] for j in range(9)] for i in range(9)]  # Copy of unsolved Sudoku
        print("Unsolved Sudoku:")
        self.print_grid(unsolved_sudoku)
        
        print("Initialization:")
        self.print_possibilities()  # Print initial possibilities matrix
        
        iteration = 1  # Start from iteration 1
        while not self.is_solved():
            previous_grid = [row[:] for row in self.grid]  # Copy of current grid state
            self.propagate_constraints()
            self.fill_single_possibility()  # Apply the solving strategy
            
            if previous_grid == self.grid:
                print(f"Stuck at iteration: {iteration}")
                break  # Prevent infinite loop if no progress is made

            print(f"Iteration: {iteration}")
            self.print_possibilities()
            iteration += 1
        
        end_time = time.time()  # End timing
        total_time = end_time - start_time  # Calculate the time taken
        
        if self.is_solved():
            solved_sudoku = [[self.grid[i][j] for j in range(9)] for i in range(9)]  # Copy of solved Sudoku
            print("\nSolved Sudoku:")
            self.print_grid(solved_sudoku)
        else:
            print("\nUnable to solve Sudoku with current strategy.")
        
        print(f"Time taken: {total_time:.2f} seconds")
        print(f"Iterations: {iteration - 1}")

    def fill_single_possibility(self):
        # Fill cells where only one possibility exists
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0 and sum(self.possibilities[i][j]) == 1:
                    self.grid[i][j] = self.possibilities[i][j].index(1) + 1

    def print_possibilities(self):
        # Print the possibilities matrix
        for i in range(9):
            for j in range(9):
                print(f"Cell ({i}, {j}): {self.possibilities[i][j]}")
        print()

    def print_grid(self, sudoku):
        # Print the Sudoku grid
        for row in sudoku:
            print(row)
        print()

# Define the puzzles
default_puzzle = [
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

easy_puzzle = [
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

medium_puzzle = [
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

hard_puzzle = [
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

def solve_puzzles(puzzles):
    # Solve each puzzle in the provided dictionary
    for difficulty, puzzle in puzzles.items():
        print(f"Solving {difficulty} puzzle:\n")
        solver = SudokuSolver(puzzle)
        solver.solve()
        print("\n" + "="*50 + "\n")

# Define the puzzles
puzzles = {
    "default": default_puzzle,
    "easy": easy_puzzle,
    "medium": medium_puzzle,
    "hard": hard_puzzle
}

solve_puzzles(puzzles)