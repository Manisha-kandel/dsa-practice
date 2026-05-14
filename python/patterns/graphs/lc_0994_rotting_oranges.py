
'''
994. Rotting Oranges, 20 minutes
'''
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #if impossible(if any fresh is surrounded by empty cells), return -1  
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        #keep count of fresh oranges, udpate queue with rotten items cell
        for r in range(ROWS):  
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        # MULTI-SOURCE BFS
        directions = [[0,1], [0,-1], [1,0], [-1, 0]]
        while q and fresh > 0:  #q:rotten orange cells in this layer of BFS, fresh: count of fresh oranges remaining      
            for i in range(len(q)):   
                r, c = q.popleft()    #rotten
                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    #if in bounds and fresh, make rotten
                    if (row < 0 or row == ROWS or  \
                        col < 0 or col == COLS or  \
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1