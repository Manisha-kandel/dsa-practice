'''
695. Max Area of Island, 25 mintues
'''
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Use visit = set() to keep track of the visited land cells
        #We should use dfs to find area

        visit = set()   #(r,c) pairs
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [
                      [0,1],
                      [0,-1],
                      [1,0],
                      [-1,0]
                    ]
        def dfs(row, col): #->add the 1 cells to visit,  gives area,  
            if (row < 0 or col < 0 or row == ROWS or col == COLS \
                or grid[row][col] == 0 or (row,col) in visit):  #if these, return 0 immediately
                return 0
            visit.add((row,col))     #else, add cell to visit
            area = 1                 #start counting area

            for dr, dc in directions:
                area += dfs(row+dr, col+dc)

            return area 


        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:  #new island found
                    area = dfs(r,c)                         #it's area
                    max_area = max(area, max_area)          #max_area till now

        return max_area