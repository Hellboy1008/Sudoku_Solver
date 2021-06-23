# Created by: 龍ONE
# Date Created: June 15, 2021
# Date Edited: June 22, 2021
# Purpose: Test the sudoku solver on puzzles of different difficulty levels.

import SudokuSolver as solver

# read problem file
problems_file = open('./test_files/sudoku_problems.txt')
tests = problems_file.read().split('\n---------\n')
tests = [row.replace('\n', ',') for row in tests]
tests = [row.split(',') for row in tests]
tests = [[[int(char) for char in row] for row in test] for test in tests]

# solve test puzzles
for test in tests:
    solver.solveSudoku(test)

# read solution file
solutions_file = open('./test_files/sudoku_solutions.txt')

# check program solutions with solution file
