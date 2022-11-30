# Created by: 龍ONE
# Date Created: November 26, 2022
# Date Edited: November 29, 2022
# Purpose: PencilMark object used to solve sudoku board.

class PencilMark:

    # constants
    BOX_NUMS = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
                [3, 4, 5, 12, 13, 14, 21, 22, 23],
                [6, 7, 8, 15, 16, 17, 24, 25, 26],
                [27, 28, 29, 36, 37, 38, 45, 46, 47],
                [30, 31, 32, 39, 40, 41, 48, 49, 50],
                [33, 34, 35, 42, 43, 44, 51, 52, 53],
                [54, 55, 56, 63, 64, 65, 72, 73, 74],
                [57, 58, 59, 66, 67, 68, 75, 76, 77],
                [60, 61, 62, 69, 70, 71, 78, 79, 80]]
    BOX_SIZE = 3
    COL_NUMS = [[0, 9, 18, 27, 36, 45, 54, 63, 72],
                [1, 10, 19, 28, 37, 46, 55, 64, 73],
                [2, 11, 20, 29, 38, 47, 56, 65, 74],
                [3, 12, 21, 30, 39, 48, 57, 66, 75],
                [4, 13, 22, 31, 40, 49, 58, 67, 76],
                [5, 14, 23, 32, 41, 50, 59, 68, 77],
                [6, 15, 24, 33, 42, 51, 60, 69, 78],
                [7, 16, 25, 34, 43, 52, 61, 70, 79],
                [8, 17, 26, 35, 44, 53, 62, 71, 80]]
    GRID_SIZE = 9
    INITIAL_PM = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ROW_NUMS = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
                [9, 10, 11, 12, 13, 14, 15, 16, 17],
                [18, 19, 20, 21, 22, 23, 24, 25, 26],
                [27, 28, 29, 30, 31, 32, 33, 34, 35],
                [36, 37, 38, 39, 40, 41, 42, 43, 44],
                [45, 46, 47, 48, 49, 50, 51, 52, 53],
                [54, 55, 56, 57, 58, 59, 60, 61, 62],
                [63, 64, 65, 66, 67, 68, 69, 70, 71],
                [72, 73, 74, 75, 76, 77, 78, 79, 80]]

    def __init__(self, board):
        ''' Initialize pencil marks for a new sudoku board.

        Args:
            board (list): Sudoku board
        '''

        # initialize pencil marks
        self.pm = {}
        pm_count = 0
        for r_index in range(self.GRID_SIZE):
            for c_index in range(self.GRID_SIZE):
                if board[r_index][c_index] == 0:
                    self.pm[pm_count] = self.INITIAL_PM
                else:
                    self.pm[pm_count] = []
                pm_count += 1

        # scan pencil marks
        pm_count = 0
        for r_index in range(self.GRID_SIZE):
            for c_index in range(self.GRID_SIZE):
                if board[r_index][c_index] != 0:
                    self.updatePM(pm_count, board[r_index][c_index])
                pm_count += 1

    def getPMInfo(self, keys):
        ''' Retrieve a dictionary provided pencil marks and their
            positions given a set of keys (box, col, row).

        Args:
            keys (list): Keys to be searched

        Returns:
            pm_info (dict): Dictionary containing pencil mark
                            information
        '''
        pm_info = {}
        for key in keys:
            for mark in self.pm[key]:
                if mark not in pm_info:
                    pm_info[mark] = [key]
                else:
                    pm_info[mark].append(key)
        return pm_info

    def printPM(self):
        ''' Print pencil marks.
        '''
        print('PENCIL_MARKS:')
        for num in range(0, self.GRID_SIZE * self.GRID_SIZE):
            print(self.pm[num], end='')
            if num % self.GRID_SIZE == self.GRID_SIZE - 1:
                print()
                continue
            print(', ', end='')

    def updatePM(self, target_key, val, changeBox=True,
                 changeCol=True, changeRow=True, excludeKeys=[],
                 getChanges=False):
        ''' Update pencil marks given a value to be removed
            and the location of that value.

        Args:
            target_key (int): Location of the value to be removed
            val (int): Value to be removed from pencil marks
            changeBox (boolean): Whether pencil marks in boxes should 
                                 be changed, default value is True
            changeCol (boolean): Whether pencil marks in columns should 
                                 be changed, default value is True
            changeRow (boolean): Whether pencil marks in rows should 
                                 be changed, default value is True
            excludeKeys (list): Keys to exclude from update, default
                                value is empty list
            getChanges (boolean): Whether to return a list filled 
                                  with keys and values before update, 
                                  default value is True

        Returns:
            before_changes (list): Returns list of keys and values before
                                   pencil marks were updated.\
        '''
        change_keys = []
        # get keys for corresponding box
        if changeBox:
            for box in self.BOX_NUMS:
                if target_key in box:
                    box_change_keys = box
                    break
            change_keys.extend(box_change_keys)
        # get keys for corresponding column
        if changeCol:
            for col in self.COL_NUMS:
                if target_key in col:
                    col_change_keys = col
                    break
            change_keys.extend(col_change_keys)
        # get keys for corresponding row
        if changeRow:
            for row in self.ROW_NUMS:
                if target_key in row:
                    row_change_keys = row
                    break
            change_keys.extend(row_change_keys)

        # exclude keys if needed
        if len(excludeKeys) != 0:
            change_keys = [key for key in change_keys
                           if key not in excludeKeys]

        # remove value from pencil marks
        before_changes = []
        for key in change_keys:
            if getChanges and val in self.pm[key]:
                before_changes.append((key, self.pm[key]))
            self.pm[key] = [mark for mark in self.pm[key] if mark != val]

        return before_changes
