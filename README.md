# Exploring Belief Propagation and Alternative Algorithms for Sudoku Solving

## Overview
This repository contains Python scripts implementing various Sudoku-solving algorithms with different approaches. Each script provides unique methods and functionalities for solving Sudoku puzzles, ranging from GUI-based interactive solvers to algorithmic solutions like backtracking, belief propagation, and constraint propagation.

---

## Files and Contents

### 1. **backtracking.py**
   - **Description:** 
     - Implements a graphical Sudoku solver using a Tkinter GUI and the backtracking algorithm.
   - **Key Features:**
     - GUI-based interactive Sudoku puzzle input.
     - Predefined puzzles of different difficulties (default, easy, medium, hard).
     - Recursive backtracking algorithm for solving Sudoku puzzles.
     - Tracks and displays solving time and iterations.
   - **Usage:** 
     - Run the script to open the Sudoku solver GUI.
     - Load a puzzle or input values manually, then click "Solve."

---

### 2. **belief_propagation.py**
   - **Description:**
     - Provides a Sudoku solver that uses the belief propagation algorithm.
   - **Key Features:**
     - GUI-based solver similar to `backtracking.py`.
     - Implements belief propagation for updating probabilities in the grid.
     - Falls back to backtracking if belief propagation does not converge.
     - Supports predefined puzzles and interactive input.
   - **Usage:** 
     - Run the script to open the GUI.
     - Solve puzzles using belief propagation or backtracking as a fallback.

---

### 3. **constraint_propagation.py**
   - **Description:**
     - Implements a Sudoku solver using constraint propagation.
   - **Key Features:**
     - Text-based solver without GUI.
     - Propagates constraints from Sudoku rules to eliminate invalid numbers.
     - Tracks solving process with step-by-step iterations and possibilities matrix.
     - Solves predefined puzzles of varying difficulties (default, easy, medium, hard).
   - **Usage:** 
     - Run the script to solve predefined puzzles.
     - The solving process and results will be displayed in the console.

---

## How to Use
1. **Backtracking Solver:** Use `backtracking.py` for a GUI-based interactive Sudoku solving experience.
2. **Belief Propagation Solver:** Use `belief_propagation.py` for a GUI-based solver with advanced probabilistic techniques.
3. **Constraint Propagation Solver:** Use `constraint_propagation.py` for a text-based, step-by-step approach.

---

## Requirements
- Python 3.x
- Required libraries:
  - `tkinter` (for GUI-based scripts)
  - `numpy` (for `belief_propagation.py`)
- Additional libraries may be installed via pip if not available.

---
