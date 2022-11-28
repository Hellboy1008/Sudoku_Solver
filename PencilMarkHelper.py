# Created by: 龍ONE
# Date Created: October 14, 2020
# Date Edited: November 27, 2022
# Purpose: Holds functions for creating and manipulating
#          pencil marks in sudoku puzzle.

import copy
import time
from PencilMark import PencilMark

# constants
GRID_SIZE = 9
PAIR_SIZE = 2


def checkDuplicates(arr, size):
    ''' Check if items in a dictionary have duplicate values.

    Args:
        arr (list): List of dictionary items to be searched
        size (int): Length of duplicate value

    Returns:
        [list]: List of keys with duplicate values if found, 
                otherwise empty list
        [list]: Duplicate list if found, otherwise empty list
    '''
    for key, value in arr:
        for key2, value2 in arr:
            if key == key2:
                continue
            if value == value2 and len(value) == size:
                return [key, key2], value
    return [], []


def checkSolved(board):
    ''' Check if sudoku board is solved.

    Args:
        board (list): Sudoku board

    Returns:
        [boolean]: True if sudoku is solved, false otherwise
    '''
    for row in board:
        if 0 in row:
            return False
    return True


def hiddenSingles(board, pencil_marks):
    ''' Find hidden singles in pencil marks and fill in the
        sudoku board accordingly.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    '''
    # find hidden singles in each row
    hiddenSinglesHelper(board, pencil_marks, pencil_marks.ROW_NUMS)
    # find hidden singles in each col
    hiddenSinglesHelper(board, pencil_marks, pencil_marks.COL_NUMS)
    # find hidden singles in each box
    hiddenSinglesHelper(board, pencil_marks, pencil_marks.BOX_NUMS)


def hiddenSinglesHelper(board, pencil_marks, target_keys):
    ''' Filter out hidden singles for a given set of target
        keys and fill in sudoku board accordingly.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
        target_keys (list): specific collections of a set of keys
    '''
    for keys in target_keys:
        pm_info = pencil_marks.getPMInfo(keys)
        for mark in pm_info.keys():
            if len(pm_info[mark]) == 1:
                row_index = pm_info[mark][0] // pencil_marks.GRID_SIZE
                col_index = pm_info[mark][0] % pencil_marks.GRID_SIZE
                board[row_index][col_index] = mark
                pencil_marks.pm[pm_info[mark][0]] = []
                pencil_marks.updatePM(pm_info[mark][0], mark)


def findPairs(pencil_marks):
    ''' Find pairs (obvious or hidden) in pencil marks and fill 
        in the sudoku board accordingly.

    Args:
        pencil_marks (list): Pencil marks for sudoku board
    '''
    # find pairs for boxs
    findPairsHelper(pencil_marks, pencil_marks.BOX_NUMS,
                    changeCol=False, changeRow=False)

    # find pairs for columns
    findPairsHelper(pencil_marks, pencil_marks.COL_NUMS,
                    changeBox=False, changeRow=False)

    # find pairs for rows
    findPairsHelper(pencil_marks, pencil_marks.ROW_NUMS,
                    changeBox=False, changeCol=False)


def findPairsHelper(pencil_marks, target_keys, changeBox=True,
                    changeCol=True, changeRow=True):
    ''' Filter out pairs for a given set of target keys and
        fill in sudoku board accordingly.

    Args:
        pencil_marks (list): Pencil marks for sudoku board
        target_keys (list): specific collections of a set of keys
        changeBox (boolean): Whether pencil marks in boxs should 
                             be changed, default value is True
        changeCol (boolean): Whether pencil marks in columns should 
                             be changed, default value is True
        changeRow (boolean): Whether pencil marks in rows should 
                             be changed, default value is True
    '''
    for keys in target_keys:
        pm_info = pencil_marks.getPMInfo(keys)
        duplicates, duplicate_keys = checkDuplicates(pm_info.items(),
                                                     PAIR_SIZE)
        if len(duplicates) != 0:
            pencil_marks.pm[duplicate_keys[0]] = duplicates
            pencil_marks.pm[duplicate_keys[1]] = duplicates
            pencil_marks.updatePM(duplicate_keys[0], duplicates[0],
                                  changeBox=changeBox,
                                  changeCol=changeCol, changeRow=changeRow,
                                  excludeKeys=duplicate_keys)
            pencil_marks.updatePM(duplicate_keys[0], duplicates[1],
                                  changeBox=changeBox,
                                  changeCol=changeCol, changeRow=changeRow,
                                  excludeKeys=duplicate_keys)


def obviousSingles(board, pencil_marks):
    ''' Find obvious singles in pencil marks and fill in the
        sudoku board accordingly.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    '''
    for key in pencil_marks.pm.keys():
        if len(pencil_marks.pm[key]) == 1:
            row_index = key // pencil_marks.GRID_SIZE
            col_index = key % pencil_marks.GRID_SIZE
            board[row_index][col_index] = pencil_marks.pm[key][0]
            pencil_marks.updatePM(key, board[row_index][col_index])


def solve(board, pencil_marks):
    ''' Solves the sudoku board using solving techniques.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    '''
    # solves sudoku puzzle using pencil marks
    start_time = time.time()
    x = 0
    while not checkSolved(board):
        obviousSingles(board, pencil_marks)
        hiddenSingles(board, pencil_marks)
        findPairs(pencil_marks)
        x += 1
        if x == 50:
            break
    end_time = time.time()
    print('TIME_TAKEN', end_time - start_time)
    print('ROUNDS', x)
    print('BOARD:')
    for row in board:
        print(row)
    pencil_marks.printPM()
