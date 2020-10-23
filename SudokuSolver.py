# Created by: 龍ONE
# Date Created: October 14, 2020
# Date Edited: October 15, 2020
# Purpose: To solve sudoku puzzles ranging in all levels, from beginner to expert.

# import other python files
import PencilMarks as pencilmarks
import BruteForce as bruteforce

# ask for user input
valid_board = False
while valid_board == False:
    sudoku_board = []
    print('Input the sudoku board from the top row to the bottom row. \nRepresent blanks with the number 0 and leave no spaces between each number.')
    # ask for values in each row
    for row in range(1, 10):
        input_row = input('Row ' + str(row) + ': \n')
        sudoku_board.append(input_row.strip())
    # check to make sure user input was valid
    for row in sudoku_board:
        # check if each row has 9 numbers and check that the numbers are between 0-9
        if len(row) == 9 and row.isdigit():
            valid_board = True
        else:
            valid_board = False
            break
    # if the board was invalid, ask user to input again
    if valid_board == False:
        print('There was something from with your input. Please try again.\n')

# covert sudoku board to proper two-dimensional structure
sudoku_board = [[int(char) for char in row] for row in sudoku_board]

# run conventional solve 20 times
for count in range(0, 20):
    pencilmarks.solveSudoku(sudoku_board)
    # loop through board to see if solved
    solved = True
    for row in sudoku_board:
        # check if there are unsolved numbers in the sudoku
        if 0 in row:
            solved = False
    # check if solved
    if solved == True:
        break

# loop through sudoku board to check if solved
solved = True
for row in sudoku_board:
    # check if there are unsolved numbers in the sudoku
    if 0 in row:
        solved = False

# if sudoku board is not solved, run brute force algorithm
if solved == False:
    print('ERROR')

# print solution for sudoku board
print('\nSolution for sudoku board:\n')
sudoku_board = [[str(num) for num in row] for row in sudoku_board]
for row in sudoku_board:
    print("".join(row))
