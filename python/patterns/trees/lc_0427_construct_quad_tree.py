# 427. Construct Quad Tree - 15 minutes
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        #each internal node in tree: it's like a node in the grid, the leaves / branches emerging from it represents the four quads that it divides the grid into.
        #we keep extending a node until all it's leaves are pure (i.e. all 0s or all 1s)
        
        def dfs(n, r, c):    #helper fcn that returns the Node
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break
            
            if allSame:             #if it's a leaf, return Node(val=grid[r][c], True) 
                return Node(grid[r][c], True) 
            
            n = n // 2              #if not a leaf, assign four children nodes and return Node
            topLeft = dfs(n,r,c)
            topRight = dfs(n,r,c+n)
            bottomLeft = dfs(n, r+n, c)
            bottomRight = dfs(n, r+n, c+n)
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)      #return root Node | we could do Node(1, ... as well)  --> both are okay
        return dfs(len(grid), 0, 0)    