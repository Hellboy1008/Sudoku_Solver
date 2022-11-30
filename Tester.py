# Created by: 龍ONE
# Date Created: June 15, 2021
# Date Edited: November 29, 2022
# Purpose: Test the sudoku solver with puzzles of different difficulty levels.

import SudokuSolver as solver

# read problem file
problems_file = open('./test_files/sudoku_problems.txt')
tests = problems_file.read().split('\n---------\n')
tests = [row.replace('\n', ',') for row in tests]
tests = [row.split(',') for row in tests]
tests = [[[int(char) for char in row] for row in test] for test in tests]

# read solution file
solutions_file = open('./test_files/sudoku_solutions.txt')
solutions = solutions_file.read().split('\n---------\n')
solutions = [row.replace('\n', ',') for row in solutions]
solutions = [row.split(',') for row in solutions]
solutions = [[[int(char) for char in row] for row in solution]
             for solution in solutions]

# solve test puzzles and check with solutions
for index, test in enumerate(tests):
    solved_board = solver.solveSudoku(test)
    if solved_board == solutions[index]:
        print('Test', index + 1, 'Successful')
