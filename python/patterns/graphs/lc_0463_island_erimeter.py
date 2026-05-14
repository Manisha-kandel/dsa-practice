'''
463. Island Perimeter, 20 minutes
'''
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #exactly one island, perimeter = ?
        #we use dfs to go from one land cell to all the cells in 4 possible directions: up,  down, left and right -> dfs will return the perimeter in that direction. 
        #we need to find a land, then once we find it we start dfs from here, which gives the required perimter. 
        #(since there is a single island only, we can just check each cell -> didn't work)

        visit = set()          #don't double count periphery of same cell
        ROWS = len(grid)       
        COLS = len(grid[0])

        def dfs(i, j):
            if i == ROWS or j == COLS or i < 0 or j < 0 or grid[i][j] == 0: #is a periphery
                return 1
            if (i,j) in visit:  #is not a periphery
                return 0
            
            visit.add((i, j))
            perimeter = dfs(i, j+1)   #4 directions perimeter added together. 
            perimeter += dfs(i, j-1) 
            perimeter += dfs(i+1, j)  
            perimeter += dfs(i-1, j) 
            
            return perimeter
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:         # in the grid once we find a land cell, we do dfs (which finds perimeter in all 4 directions and give the sum) 
                    return dfs(r,c)
