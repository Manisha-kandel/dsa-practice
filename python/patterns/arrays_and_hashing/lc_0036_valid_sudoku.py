'''
36. Valid Sudoku
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #there are 9 rows, 9 cols, 9 boxes
        #create 9 arrays for rows, 9 arrays for cols, 9 arrays for boxes with size of 9 each, which will hold hold bool for if sth has been already there or not. 
        #if at any point we find that, we have a number in the cell we are checking and it already was bool in either the row array, the col array or the box array, then we return false. 
        #else, if we complete the loop of 81 cells without going to such case, we return true

        #keep track of the numbers in rows, cols and 3*3 boxes
        row_bools = [[False]*9 for i in range(9)]   
        col_bools = [[False]*9 for i in range(9)]
        box_bools = [[[False]*9 for i in range(3)] for j in range(3)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = int(board[r][c]) 
                    #if already in the same row, return False
                    if row_bools[r][num-1] == True:
                        return False
                    #already in col
                    if col_bools[c][num-1] == True:
                        return False
                    #already in box
                    if box_bools[r//3][c//3][num-1] == True:
                        return False

                    #else, set that number position: num-1 to True for row_bool, col_bool and box_bool
                    row_bools[r][num-1] = True
                    col_bools[c][num-1] = True
                    box_bools[r//3][c//3][num-1] = True

        return True