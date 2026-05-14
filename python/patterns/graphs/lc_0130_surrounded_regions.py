''' 
130. Surrounded Regions, 15 minutes
'''
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def capture_boundary(r,c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"  #immune
            capture_boundary(r+1, c)
            capture_boundary(r-1, c)
            capture_boundary(r, c+1)
            capture_boundary(r, c-1)

        # 1. (DFS) capture unsurrounded regions ( O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] =="O" and \
                    (r in [0, ROWS-1] or c in [0, COLS-1])): #in boundary cells
                    capture_boundary(r,c)
            
        # 2. Capture surrounded regions ( O-> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"