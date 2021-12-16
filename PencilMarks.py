# Created by: 龍ONE
# Date Created: October 14, 2020
# Date Edited: December 17, 2021
# Purpose: Holds functions for creating and manipulating pencil marks in sudoku puzzle.

import copy


def checkBox(board, pencil_marks):
    """ Updates pencil marks for the sudoku board by looking at 
        individual boxes and eliminating values that already 
        exist in that box.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """
    # remove existing values from pencil marks in each box
    for row_index_i in range(0, len(board), 3):
        for column_index_i in range(0, 9, 3):
            exists = []
            # loop through board
            for row_index_j in range(row_index_i, row_index_i + 3):
                for column_index_j in range(column_index_i, column_index_i + 3):
                    if board[row_index_j][column_index_j] != 0:
                        exists.append(board[row_index_j][column_index_j])
            # loop through pencil marks
            for row_index_k in range(row_index_i, row_index_i + 3):
                for column_index_k in range(column_index_i, column_index_i + 3):
                    pencil_marks[row_index_k][column_index_k] = [
                        num for num in pencil_marks[row_index_k][column_index_k] if num not in exists]


def checkColumn(board, pencil_marks):
    """ Updates pencil marks for the sudoku board by looking at 
        individual columns and eliminating values that already 
        exist in that column.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """
    # remove existing values from pencil marks in each column
    board_transpose = list(zip(*copy.deepcopy(board)))
    for index_i, column in enumerate(board_transpose):
        exists = [num for num in column if num != 0]
        for index_j, mark in enumerate(pencil_marks):
            if len(mark[index_i]) != 0:
                pencil_marks[index_j][index_i] = [
                    num for num in mark[index_i] if num not in exists]


def checkRow(board, pencil_marks):
    """ Updates pencil marks for the sudoku board by looking at 
        individual rows and eliminating values that already 
        exist in that row.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """
    # remove existing values from pencil marks in each row
    for index_i, row in enumerate(board):
        exists = [num for num in row if num != 0]
        for index_j, mark in enumerate(pencil_marks[index_i]):
            if len(mark) != 0:
                pencil_marks[index_i][index_j] = [
                    num for num in mark if num not in exists]


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


def hiddenSingles(board, pencil_marks):
    """ Find hidden singles for the sudoku board.
        Hidden singles are boxes that can only contain
        one single digit in each row, column, or box
        per the pencil marks.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """
    # check rows
    for index_i, row in enumerate(pencil_marks):
        digits = dict()
        singles = []
        # count how many times each digit appears in row
        for mark in row:
            for num in mark:
                if num not in digits:
                    digits[num] = 1
                else:
                    digits[num] += 1
        # search to see if there are any hidden singles
        for num in digits:
            if digits[num] == 1:
                singles.append(num)
        # fill board with hidden singles
        if len(singles) != 0:
            for index_j, mark in enumerate(row):
                for digit in singles:
                    if digit in mark:
                        board[index_i][index_j] = digit
                        pencil_marks[index_i][index_j] = []

    # check columns

    # check boxes

    return 0


def initializePencilMarks(board):
    """ Initialize pencil marks for a new sudoku board

    Args:
        board (list): Sudoku board

    Returns:
        [list]: Default pencil marks for sudoku board
    """
    pencil_marks = [[[1, 2, 3, 4, 5, 6, 7, 8, 9]
                     if board[row][column] == 0 else [] for column in range(9)] for row in range(9)]

    return pencil_marks


def obviousSingles(board, pencil_marks):
    """ Find obvious singles for the sudoku board.
        Obvious singles are boxes that can only contain
        one single digit as per the pencil marks.

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """

    for index_i, row in enumerate(pencil_marks):
        for index_j, mark in enumerate(row):
            if len(mark) == 1:
                board[index_i][index_j] = mark[0]
                pencil_marks[index_i][index_j] = []

    return 0


def updatePencilMarks(board, pencil_marks):
    """ Update pencil marks for the sudoku board

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """
    checkRow(board, pencil_marks)
    checkColumn(board, pencil_marks)
    checkBox(board, pencil_marks)


def solve(board, pencil_marks):
    """ Solves the sudoku board using solving techniques

    Args:
        board (list): Sudoku board
        pencil_marks (list): Pencil marks for sudoku board
    """
    # solves sudoku puzzle using pencil marks
    while not checkSolved(board):
        updatePencilMarks(board, pencil_marks)
        obviousSingles(board, pencil_marks)
        updatePencilMarks(board, pencil_marks)
        hiddenSingles(board, pencil_marks)
    #print(pencil_marks)
    #print(board)
    #print(pencil_marks)
