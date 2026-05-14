'''
417. Pacific Atlantic Water Flow, 25 minutes
'''
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # we find those grids which will flow to pacific
        #// for atlantic
        #return those which are in both
        ROWS, COLS = len(heights), len(heights[0])
        visit_pac, visit_atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or heights[r][c] < prevHeight):
                return
            visit.add((r,c))         #visit (this is the core task of dfs), that's it, later we use visited to get result (visit has all the points, already visited but also can reach to pacific)
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, visit_pac, heights[0][c])   # Top edge (Pacific)
            dfs(ROWS-1, c, visit_atl, heights[ROWS-1][c]) # Bottom edge (Atlantic)

        for r in range(ROWS):
            dfs(r, 0, visit_pac, heights[r][0]) #left edge (pacific)
            dfs(r, COLS - 1, visit_atl, heights[r][COLS-1]) #right edge (atlantic) 

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visit_pac and (r,c) in visit_atl:
                    res.append([r,c])
        
        return res