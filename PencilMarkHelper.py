# Created by: 龍ONE
# Date Created: October 14, 2020
# Date Edited: November 26, 2022
# Purpose: Holds functions for creating and manipulating
#          pencil marks in sudoku puzzle.

import copy
import time
from PencilMark import PencilMark

# constants
GRID_SIZE = 9
BOX_SIZE = 3
INITIAL_PENCIL_MARKS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


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
    for r_index in range(0, GRID_SIZE, BOX_SIZE):
        for c_index in range(0, GRID_SIZE, BOX_SIZE):
            box_arr.append([arr[r_index][c_index], arr[r_index][c_index+1],
                            arr[r_index][c_index+2], arr[r_index+1][c_index],
                            arr[r_index+1][c_index+1],
                            arr[r_index+1][c_index+2],
                            arr[r_index+2][c_index], arr[r_index+2][c_index+1],
                            arr[r_index+2][c_index+2]])
    return box_arr


def findPairs(arr, obvious):
    """ Returns a list of pairs in an array of arrays

    Args:
        arr (list): Rows/Columns/Boxes of pencil marks
        obvious (boolean): Whether we are finding obvious or hidden pairs

    Returns:
        [list]: List of pairs in the array
    """
    pair_list = []
    # find obvious pairs
    if obvious:
        pairs = {}
        for mark in arr:
            if len(mark) == 2 and str(mark) in pairs:
                pairs[str(mark)][1] += 1
            elif len(mark) == 2:
                pairs[str(mark)] = [mark, 1]
        for p_mark in pairs:
            if pairs[p_mark][1] == 2:
                pair_list.append(pairs[p_mark][0])

    return pair_list


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
    for m_index, mark in enumerate(arr):
        for value in mark:
            if value not in dict_values:
                dict_values[value] = [m_index]
            else:
                dict_values[value].append(m_index)

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
    for b_index, box in enumerate(arr_box):
        if b_index == num:
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
    for c_index, column in enumerate(arr_transpose):
        if c_index == num:
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
    for r_index, row in enumerate(arr):
        if r_index == num:
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
    for row in range(0, GRID_SIZE):
        unique = findUnique(getRow(pencil_marks, row))
        for value in unique:
            board[row][value[1]] = value[0]
            pencil_marks[row][value[1]] = []
            updatePencilMarks(value[1], value[0], pencil_marks, row)

    # iterate columns to find hidden singles
    for col in range(0, GRID_SIZE):
        unique = findUnique(getColumn(pencil_marks, col))
        for value in unique:
            board[value[1]][col] = value[0]
            pencil_marks[value[1]][col] = []
            updatePencilMarks(col, value[0], pencil_marks, value[1])

    # iterate boxes to find hidden singles
    for box in range(0, GRID_SIZE):
        unique = findUnique(getBox(pencil_marks, box))
        for value in unique:
            box_row = box // BOX_SIZE * BOX_SIZE + value[1] // BOX_SIZE
            box_col = box % BOX_SIZE * BOX_SIZE + value[1] % BOX_SIZE
            board[box_row][box_col] = value[0]
            pencil_marks[box_row][box_col] = []
            updatePencilMarks(box_col, value[0], pencil_marks, box_row)
    return 0


def initializePencilMarks(board):
    """ Initialize pencil marks for a new sudoku board

    Args:
        board (list): Sudoku board

    Returns:
        [list]: Default pencil marks for sudoku board
    """

    # initialize pencil mark with all digits
    pencil_marks = [[INITIAL_PENCIL_MARKS
                     if board[row][column] == 0 else []
                     for column in range(GRID_SIZE)]
                    for row in range(GRID_SIZE)]

    # eliminate unnecessary pencil marks from rows
    for r_index in range(0, GRID_SIZE):
        row = getRow(pencil_marks, r_index)
        setRow([[num for num in mark if num not in getRow(board, r_index)]
                for mark in row], r_index, pencil_marks)

    # eliminate unnecessary pencil marks from columns
    for c_index in range(0, GRID_SIZE):
        column = getColumn(pencil_marks, c_index)
        setColumn([[num for num in mark if num not in getColumn(board, c_index)]
                   for mark in column], c_index, pencil_marks)

    # eliminate unnecessary pencil marks from boxes
    for b_index in range(0, GRID_SIZE):
        box = getBox(pencil_marks, b_index)
        setBox([[num for num in mark if num not in getBox(board, b_index)]
                for mark in box], b_index, pencil_marks)

    return pencil_marks


def obviousPairs(pencil_marks):
    """ Find obvious pairs for the sudoku board.
        Obvious pairs are two boxes in the same row,
        column, or box that can only contain the same two digits 
        in the pencil marks.

    Args:
        pencil_marks (list): Pencil marks for sudoku board
    """
    # iterate rows to find obvious pairs
    for r_index, row in enumerate(pencil_marks):
        pair_list = findPairs(row, True)
        if len(pair_list) == 0:
            continue
        for pair in pair_list:
            for c_index, col in enumerate(row):
                if col != pair:
                    pencil_marks[r_index][c_index] = [
                        val for val in col if val not in pair]

    # iterate columns to find obvious pairs
    for c_index in range(0, GRID_SIZE):
        col = getColumn(pencil_marks, c_index)
        pair_list = findPairs(col, True)
        if len(pair_list) == 0:
            continue
        for pair in pair_list:
            for r_index, row in enumerate(col):
                if row != pair:
                    pencil_marks[r_index][c_index] = [
                        val for val in row if val not in pair]

    # iterate boxes to find obvious pairs
    for b_index in range(0, GRID_SIZE):
        box = getBox(pencil_marks, b_index)
        pair_list = findPairs(box, True)
        if len(pair_list) == 0:
            continue
        for pair in pair_list:
            for s_index, square in enumerate(box):
                if square != pair:
                    row = b_index // BOX_SIZE * BOX_SIZE + s_index // BOX_SIZE
                    col = b_index % BOX_SIZE * BOX_SIZE + s_index % BOX_SIZE
                    pencil_marks[row][col] = [
                        val for val in square if val not in pair]


def obviousSingles(board, pencil_marks):
    """ Find obvious singles for the sudoku board.
        Obvious singles are boxes that can only contain
        one single digit as per the pencil marks.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """
    # search for one length pencil marks
    for r_index, row in enumerate(pencil_marks):
        for c_index, mark in enumerate(row):
            if len(mark) == 1:
                board[r_index][c_index] = mark[0]
                pencil_marks[r_index][c_index] = []
                updatePencilMarks(c_index, mark[0], pencil_marks, r_index)


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
    for b_index in range(len(pencil_marks_box)):
        if b_index == num:
            pencil_marks_box[b_index] = new_arr
    # replace old pencil marks with new pencil marks
    new_pencil_marks = convertToBox(pencil_marks_box)
    for pm_index in range(len(pencil_marks)):
        pencil_marks[pm_index] = new_pencil_marks[pm_index]


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
    for c_index in range(len(pencil_marks_transpose)):
        if c_index == num:
            pencil_marks_transpose[c_index] = new_arr
    # replace old pencil marks with new pencil marks
    new_pencil_marks = list(list(mark) for mark in zip(
        *copy.deepcopy(pencil_marks_transpose)))
    for pm_index in range(len(pencil_marks)):
        pencil_marks[pm_index] = new_pencil_marks[pm_index]


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
    for r_index in range(len(pencil_marks)):
        if r_index == num:
            pencil_marks[r_index] = new_arr


def solve(board, pencil_marks):
    """ Solves the sudoku board using solving techniques

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """
    # solves sudoku puzzle using pencil marks
    print('PENCIL_MARKS_I:')
    for row in pencil_marks:
        print(row)
    pencil_m = PencilMark(board)
    start_time = time.time()
    x = 0
    while not checkSolved(board):
        # old time = TIME_TAKEN 0.016991138458251953 ROUNDS 4
        obviousSingles(board, pencil_marks)
        hiddenSingles(board, pencil_marks)
        obviousPairs(pencil_marks)
        x += 1
        if x == 1000:
            break
    end_time = time.time()
    print('TIME_TAKEN', end_time - start_time)
    print("ROUNDS", x)
    print('BOARD:')
    for row in board:
        print(row)
    print('PENCIL_MARKS:')
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
               for box_val in
               getBox(pencil_marks, row_index // BOX_SIZE * BOX_SIZE
               + col_index // BOX_SIZE)]
    setBox(new_box, row_index // BOX_SIZE * BOX_SIZE + col_index // BOX_SIZE,
           pencil_marks)
