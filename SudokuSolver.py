# Created by: 龍ONE
# Date Created: October 14, 2020
# Date Edited: September 30, 2021
# Purpose: To solve sudoku puzzles ranging in all levels, from beginner to expert.

# import pencil mark file
import PencilMarks as pencilmarks


def main():
    """ Main method for extracting user input for sudoku board and running main solver.
    """
    valid_board = False
    # ask user to input sudoku board
    while not valid_board:
        sudoku_board = []
        print('Input the sudoku board from the top row to the bottom row. \nRepresent blanks with the number 0 and leave no spaces between each number.')
        # ask for the numbers in each row
        for row in range(1, 10):
            user_input = input('Row ' + str(row) + ':\n')
            sudoku_board.append(user_input.strip())
        # check to make sure board is valid
        for row in sudoku_board:
            valid_board = True if len(row) == 9 and row.isdigit() else False
            if not valid_board:
                break
        # send error message if sudoku board was not valid
        if not valid_board:
            print("There was something wrong with your input, please try again.\n")
    # convert sudoku to proper two-dimensional list with integers
    sudoku_board = [[int(char) for char in row] for row in sudoku_board]
    # solve sudoku
    solveSudoku(sudoku_board)


def solveSudoku(board):
    """ Solve sudoku using methods in PencilMarks.py

    Args:
        board (list): Sudoku board
    """
    # initialize pencil marks
    pencil_marks = pencilmarks.initializePencilMarks(board)
    # solve sudoku
    pencilmarks.solve(board, pencil_marks)
    
    return board


# run main method for program
if __name__ == "__main__":
    main()
