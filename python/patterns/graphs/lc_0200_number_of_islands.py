'''
200. Number of islands, 20 minutes
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #keep track of visit set while doing dfs (i.e. processing an island once a piece of land within that island is found), while traversing if we find a new land cell that isn't in visit, then we add #islands by 1 | islands += 1 |  
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0,1], [0,-1], [-1,0], [1,0]]

        def dfs(row,col):  #we only pass the land cell here
            #dfs should add all lands in this to the island in visit set, 
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if r >= 0 and c >= 0 and r < ROWS and \
                    c < COLS and grid[r][c] == "1" and \     
                    (r,c) not in visit:          #"1" is a string
                    visit.add((r,c)) 
                    dfs(r,c)
    
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":         
                    if (r,c) not in visit:
                        islands += 1
                        dfs(r,c) 

        return islands

#same concept, simpler form by gemini
'''
visit = set()
islands = 0 # Start at 0

def dfs(r, c):
    if (r < 0 or r >= ROWS or 
        c < 0 or c >= COLS or 
        grid[r][c] == "1" or # Check for string "0"
        (r, c) in visit):
        return
    
    visit.add((r, c))
    for dr, dc in directions:
        dfs(r + dr, c + dc)

for r in range(ROWS):
    for c in range(COLS):
        # Trigger DFS only for new islands
        if grid[r][c] == "1" and (r, c) not in visit:
            islands += 1
            dfs(r, c)
'''

#Another attempt
#200. Number of Islands

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #state: a cell when visited if it was already counted in any island considered, it will be in set, and hence not to be counted in future
        #traversal rule: go to all the sides from 1 cell wherever there is 1
        #guards: within the grid, and also only consider new cells which weren't considered earlier
        #hand-trace: 

        visit = set()
        islands = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            directions = [1,0], [0,1], [-1,0], [0,-1]
            if i>=0 and j>=0 and i<m and j<n:
                visit.add((i,j))
                for drn in directions:
                    r,c = i+drn[0], j+drn[1]
                    if (r>=0 and c>=0 and r<m and c<n) and (grid[r][c] == "1" and (r,c) not in visit):
                        dfs(r,c)
                        visit.add((r,c)) 
            return 


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if (i,j) not in visit:
                        dfs(i,j)
                        islands += 1
        
        return islands