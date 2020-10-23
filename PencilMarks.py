# Created by: 龍ONE
# Date Created: October 14, 2020
# Date Edited: October 23, 2020
# Purpose: Holds functions for creating and manipulating pencil marks in sudoku puzzle.


def checkRules(sudoku, pencil_marks):
    # checks row, column, and box to remove pencil marks

    # check row
    for row_index, row in enumerate(pencil_marks):
        # loops all the pencil marks in a row
        for mark_index, mark in enumerate(row):
            row[mark_index] = [num for num in mark if num not in sudoku[row_index]]

    # check column
    for col_index in range(0, 9):
        col_values = []
        # loop through all rows in sudoku
        for row in sudoku:
            # if the value is non-zero, append to list
            if row[col_index] != 0:
                col_values.append(row[col_index])
        # loop through all rows in pencil marks
        for row in pencil_marks:
            row[col_index] = [num for num in row[col_index]
                              if num not in col_values]

    # check box
    for box_row in range(0, 3):
        # loop through columns in sudoku
        for col_index in range(0, 9, 3):
            box_values = []
            # loop through the three specific rows for sudoku
            for row in range(3 * box_row, 3 * box_row + 3):
                # loop through the three specific columns for sudoku
                for col in range(col_index, col_index + 3):
                    # if the value is non-zero and doesn't already exist in list, append to list
                    if sudoku[row][col] not in box_values and sudoku[row][col] != 0:
                        box_values.append(sudoku[row][col])
            # loop through the three specific rows for pencil marks
            for row in range(3 * box_row, 3 * box_row + 3):
                # loop through the three specific columns for pencil marks
                for col in range(col_index, col_index + 3):
                    pencil_marks[row][col] = [
                        num for num in pencil_marks[row][col] if num not in box_values]

    return pencil_marks


def checkUnique(sudoku, pencil_marks):
    # check unique values in row, column, and box and changes puzzle directly

    # check row
    for row_index, row in enumerate(pencil_marks):
        numbers_count = [0] * 9
        # loop through each pencil mark in the row
        for values in row:
            # loop through each value in pencil marks
            for num in values:
                numbers_count[num - 1] += 1
        # loop through the number count
        for count_val_index, count_val in enumerate(numbers_count):
            if count_val == 1:
                # loop through all values again
                for values_index, values in enumerate(row):
                    # find the pencil mark with that value
                    if (count_val_index + 1) in values:
                        sudoku[row_index][values_index] = count_val_index + 1
                        row[values_index] = []

    # check column


def createPencilMarks(sudoku):
    # creates pencil marks for given sudoku board
    pencil_marks = []

    # fill default pencil marks for each row
    for row_index, row in enumerate(sudoku):
        pencil_marks.append([])
        # loop through all values in each row
        for value_index, value in enumerate(row):
            pencil_marks[row_index].append([])
            # add pencil marks if the value is 0
            if value == 0:
                # add all numbers from 1 to 9
                for num in range(1, 10):
                    pencil_marks[row_index][value_index].append(num)

    # remove pencil marks by checking rules
    pencil_marks = checkRules(sudoku, pencil_marks)

    return pencil_marks


def solveSudoku(sudoku):
    # solves sudoku puzzle using pencil marks
    pencil_marks = createPencilMarks(sudoku)

    # fill in sudoku by checking unique values
    checkUnique(sudoku, pencil_marks)

    # fill in sudoku by checking single values
    for row_index, row in enumerate(pencil_marks):
        for col_index, col in enumerate(row):
            if len(col) == 1:
                sudoku[row_index][col_index] = col[0]
