# Created by: 龍ONE
# Date Created: October 14, 2020
# Date Edited: November 7, 2022
# Purpose: Holds functions for creating and manipulating pencil marks in sudoku puzzle.

import copy

def checkSolved(board):
    """ Check if sudoku board is solved

    Args:
        board (list): Sudoku board

    Returns:
        [boolean]: True if sudoku is solved, false otherwise
    """
    for row in board:
        if 0 in row:
            return False
    return True


def convertToBox(arr):
    """ Returns the box version of an array

    Args:
        arr (list): Pencil marks or sudoku board

    Returns:
        [list]: Box version of specified array
    """
    # convert arr into box
    box_arr = []
    for index_i in range(0, 9, 3):
        for index_j in range(0, 9, 3):
            box_arr.append([arr[index_i][index_j], arr[index_i][index_j+1], arr[index_i][index_j+2], arr[index_i+1][index_j], arr[index_i+1]
                           [index_j+1], arr[index_i+1][index_j+2], arr[index_i+2][index_j], arr[index_i+2][index_j+1], arr[index_i+2][index_j+2]])
    return box_arr

def findUnique(arr):
    """ Returns a unique value in an array of arrays

    Args:
        arr (list): Rows/Columns/Boxes of pencil marks

    Returns:
        [list]: List of unique values in the array paired with their 
                positions in the array
    """
    # fill dictionary with pencil marks
    dict_values = {}
    for index, mark in enumerate(arr):
        for value in mark:
            if value not in dict_values:
                dict_values[value] = [index]
            else:
                dict_values[value].append(index)
        
    # determine unique value in array
    unique = []
    for key in dict_values:
        if len(dict_values[key]) == 1:
            unique.append((key, dict_values[key][0]))
                                                                                                    
    return unique


def getBox(arr, num):
    """ Returns a specific box from array

    Args:
        arr (list): Pencil marks or sudoku board
        num(int): Box number

    Returns:
        [list]: Specified box from array
    """
    # convert arr into box
    arr_box = convertToBox(arr)
    for index, box in enumerate(arr_box):
        if index == num:
            return box


def getColumn(arr, num):
    """ Returns a specific column from array

    Args:
        arr (list): Pencil marks or sudoku board
        num(int): Column number

    Returns:
        [list]: Specified column from array
    """
    # transpose arr
    arr_transpose = list(zip(*copy.deepcopy(arr)))
    for index, column in enumerate(arr_transpose):
        if index == num:
            return list(column)


def getRow(arr, num):
    """ Returns a specific row from array

    Args:
        arr (list): Pencil marks or sudoku board
        num(int): Row number

    Returns:
        [list]: Specified row from array
    """
    # return specified row
    for index, row in enumerate(arr):
        if index == num:
            return row

def hiddenSingles(board, pencil_marks):
    """ Find hidden singles for the sudoku board.
        Hidden singles are boxes where a box has to contain
        a certain number based on its row/column/box.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """
    # iterate rows to find hidden singles
    for row in range(0,9):
        unique = findUnique(getRow(pencil_marks, row))
        for value in unique:
            board[row][value[1]] = value[0]
            pencil_marks[row][value[1]] = []
            updatePencilMarks(value[1], value[0], pencil_marks, row)
            
    # iterate columns to find hidden singles
    for col in range(0,9):
        unique = findUnique(getColumn(pencil_marks, col))
        for value in unique:
            board[value[1]][col] = value[0]
            pencil_marks[value[1]][col] = []
            updatePencilMarks(col, value[0], pencil_marks, value[1])
        
    # iterate boxes to find hidden singles
    for box in range(0,9):
        unique = findUnique(getBox(pencil_marks, box))
        print("XDD", unique)
        print(getBox(pencil_marks, box))   
    return 0

def initializePencilMarks(board):
    """ Initialize pencil marks for a new sudoku board

    Args:
        board (list): Sudoku board

    Returns:
        [list]: Default pencil marks for sudoku board
    """

    # initialize pencil mark with all digits
    pencil_marks = [[[1, 2, 3, 4, 5, 6, 7, 8, 9]
                     if board[row][column] == 0 else [] for column in range(9)] for row in range(9)]

    print("ROWS:")
    # eliminate unnecessary pencil marks from rows
    for index in range(0, 9):
        row = getRow(pencil_marks, index)
        setRow([[num for num in mark if num not in getRow(board, index)]
                for mark in row], index, pencil_marks)
    for row in pencil_marks:
        print(row)
    print("COLUMNS:")
    # eliminate unnecessary pencil marks from columns
    for index in range(0, 9):
        column = getColumn(pencil_marks, index)
        setColumn([[num for num in mark if num not in getColumn(board, index)]
                   for mark in column], index, pencil_marks)
    for row in pencil_marks:
        print(row)
    print("BOXES:")
    # eliminate unnecessary pencil marks from boxes
    for index in range(0, 9):
        box = getBox(pencil_marks, index)
        setBox([[num for num in mark if num not in getBox(board, index)]
                for mark in box], index, pencil_marks)
    for row in pencil_marks:
        print(row)

    return pencil_marks

def obviousPairs(board, pencil_marks):
    return 0

def obviousSingles(board, pencil_marks):
    """ Find obvious singles for the sudoku board.
        Obvious singles are boxes that can only contain
        one single digit as per the pencil marks.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """
    # search for one length pencil marks
    for index_i, row in enumerate(pencil_marks):
        for index_j, mark in enumerate(row):
            if len(mark) == 1:
                board[index_i][index_j] = mark[0]
                pencil_marks[index_i][index_j] = []
                updatePencilMarks(index_j, mark[0], pencil_marks, index_i)


def setBox(new_arr, num, pencil_marks):
    """ Changes a specific box from pencil marks

    Args:
        new_arr (list): Updated box for pencil marks
        num(int): Bow number
        pencil_marks (list): Pencil marks for sudoku board

    Returns:
        [list]: Updated pencil marks for sudoku board
    """
    # change pencil marks to box
    pencil_marks_box = convertToBox(pencil_marks)
    # change specified box
    for index in range(len(pencil_marks_box)):
        if index == num:
            pencil_marks_box[index] = new_arr
    # replace old pencil marks with new pencil marks
    new_pencil_marks = convertToBox(pencil_marks_box)
    for index in range(len(pencil_marks)):
        pencil_marks[index] = new_pencil_marks[index]


def setColumn(new_arr, num, pencil_marks):
    """ Changes a specific column from pencil marks

    Args:
        new_arr (list): Updated column for pencil marks
        num(int): Column number
        pencil_marks (list): Pencil marks for sudoku board

    Returns:
        [list]: Updated pencil marks for sudoku board
    """
    # transpose pencil marks
    pencil_marks_transpose = list(zip(*copy.deepcopy(pencil_marks)))
    # change specified column
    for index in range(len(pencil_marks_transpose)):
        if index == num:
            pencil_marks_transpose[index] = new_arr
    # replace old pencil marks with new pencil marks
    new_pencil_marks = list(list(mark)
                            for mark in zip(*copy.deepcopy(pencil_marks_transpose)))
    for index in range(len(pencil_marks)):
        pencil_marks[index] = new_pencil_marks[index]


def setRow(new_arr, num, pencil_marks):
    """ Changes a specific row from pencil marks

    Args:
        new_arr (list): Updated row for pencil marks
        num(int): Row number
        pencil_marks (list): Pencil marks for sudoku board

    Returns:
        [list]: Updated pencil marks for sudoku board
    """
    # change specified row
    for index in range(len(pencil_marks)):
        if index == num:
            pencil_marks[index] = new_arr


def solve(board, pencil_marks):
    """ Solves the sudoku board using solving techniques

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """
    # solves sudoku puzzle using pencil marks
    x = 0
    while not checkSolved(board):
        obviousSingles(board, pencil_marks)
        hiddenSingles(board, pencil_marks)
        x += 1
        if x == 1000:
            break
    print("BOARD:")
    for row in board:
        print(row)
    print("PENCIL_MARKS:")
    for row in pencil_marks:
        print(row)


def updatePencilMarks(col_index, num, pencil_marks, row_index):
    """ Updates pencil marks by removing a value 
        from the pencil marks.

   Args:
       col_index (int): Column index for the value
       num: Value to remove from pencil marks
       pencil_marks (list): Pencil marks for sudoku board
       row_index (int): Row index for the value
   """
    # update row
    new_row = [[val for val in row_val if val not in [num]]
               for row_val in getRow(pencil_marks, row_index)]
    setRow(new_row, row_index, pencil_marks)
    # update column
    new_col = [[val for val in col_val if val not in [num]]
               for col_val in getColumn(pencil_marks, col_index)]
    setColumn(new_col, col_index, pencil_marks)
    # update box
    new_box = [[val for val in box_val if val not in [num]]
               for box_val in getBox(pencil_marks, row_index // 3 * 3 + col_index // 3)]
    setBox(new_box, row_index // 3 * 3 + col_index // 3, pencil_marks)
