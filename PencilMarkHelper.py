# Created by: 龍ONE
# Date Created: October 14, 2020
# Date Edited: November 29, 2022
# Purpose: Holds functions for creating and manipulating
#          pencil marks in sudoku puzzle.

import time

# constants
GRID_SIZE = 9
MAX_ROUNDS = 10
PAIR_SIZE = 2


def absolutes(pencil_marks):
    ''' Find absolutes in pencil marks and update pencil
        marks accordingly.

    Args:
        pencil_marks (list): Pencil marks for sudoku board
    '''
    # find row absolutes
    absolutesHelper(pencil_marks, pencil_marks.ROW_NUMS)
    # find column absolutes
    absolutesHelper(pencil_marks, pencil_marks.COL_NUMS)


def absolutesHelper(pencil_marks, target_keys):
    ''' Find absolutes for a given set of target keys and
        update pencil marks accordingly.

    Args:
        pencil_marks (list): Pencil marks for sudoku board
        target_keys (list): specific collections of a set of keys
    '''
    for keys in target_keys:
        pm_info = pencil_marks.getPMInfo(keys)
        for info_key in pm_info:
            hasAbsolute = False
            for box in pencil_marks.BOX_NUMS:
                if all(mark in box for mark in pm_info[info_key]):
                    hasAbsolute = True
                    break
            if hasAbsolute:
                pencil_marks.updatePM(pm_info[info_key][0], info_key,
                                      changeCol=False, changeRow=False,
                                      excludeKeys=pm_info[info_key])


def bruteForce(board, pencil_marks):
    ''' Use brute force method through recursion to solve
        board.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board

    Returns:
        [boolean]: True if board is solved, false otherwise
    '''
    # check to see if board is solved
    if checkSolved(board):
        return True

    # get first key with non-empty pencil marks
    key = getFirstPencilMark(pencil_marks)
    r_index = key // pencil_marks.GRID_SIZE
    c_index = key % pencil_marks.GRID_SIZE

    for mark in pencil_marks.pm[key]:
        # check if pencil marks are valid
        if checkValid(board, pencil_marks):
            board[r_index][c_index] = mark
            old_pm = pencil_marks.pm[key]
            pencil_marks.pm[key] = []
            changes = pencil_marks.updatePM(key, mark, getChanges=True)
            # recurse until board is solved
            if bruteForce(board, pencil_marks):
                return True
            else:
                board[r_index][c_index] = 0
                pencil_marks.pm[key] = old_pm
                for change in changes:
                    pencil_marks.pm[change[0]] = change[1]
    return False


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


def checkValid(board, pencil_marks):
    ''' Check if sudoku board and pencil marks are valid.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board

    Returns:
        [boolean]: True if board and pencil marks are valid,
                   false otherwise
    '''
    for key in pencil_marks.pm.keys():
        if len(pencil_marks.pm[key]) == 0:
            r_index = key // pencil_marks.GRID_SIZE
            c_index = key % pencil_marks.GRID_SIZE
            if board[r_index][c_index] == 0:
                return False
    return True


def getFirstPencilMark(pencil_marks):
    ''' Return the key of the first non-empty pencil mark.

    Args:
        pencil_marks (list): Pencil marks for sudoku board

    Returns:
        key: First non-empty pencil mark, returns -1 if
             pencil marks are empty
    '''
    for key in pencil_marks.pm.keys():
        if len(pencil_marks.pm[key]) != 0:
            return key
    return -1


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
                r_index = pm_info[mark][0] // pencil_marks.GRID_SIZE
                c_index = pm_info[mark][0] % pencil_marks.GRID_SIZE
                board[r_index][c_index] = mark
                pencil_marks.pm[pm_info[mark][0]] = []
                pencil_marks.updatePM(pm_info[mark][0], mark)


def findPairs(pencil_marks):
    ''' Find pairs (obvious or hidden) in pencil marks and update 
        pencil marks accordingly.

    Args:
        pencil_marks (list): Pencil marks for sudoku board
    '''
    # find pairs for boxes
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
        update pencil marks accordingly.

    Args:
        pencil_marks (list): Pencil marks for sudoku board
        target_keys (list): specific collections of a set of keys
        changeBox (boolean): Whether pencil marks in boxes should 
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
            r_index = key // pencil_marks.GRID_SIZE
            c_index = key % pencil_marks.GRID_SIZE
            board[r_index][c_index] = pencil_marks.pm[key][0]
            pencil_marks.updatePM(key, board[r_index][c_index])


def solve(board, pencil_marks):
    ''' Solves the sudoku board using solving techniques.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    '''
    start_time = time.time()
    rounds = 0

    # solve using traditional methods
    while not checkSolved(board):
        obviousSingles(board, pencil_marks)
        hiddenSingles(board, pencil_marks)
        findPairs(pencil_marks)
        absolutes(pencil_marks)
        rounds += 1
        if rounds == MAX_ROUNDS:
            break

    # if sudoku is not solved, use brute force method
    if not checkSolved(board):
        bruteForce(board, pencil_marks)

    # print solved board
    print('SOLUTION:')
    for row in board:
        print(row)

    end_time = time.time()
    print('Time Taken:', '{:.3f}'.format(end_time - start_time), 'seconds')
