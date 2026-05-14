'''
261. Graph Valid Tree, 20 minutes
'''
from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: 
            return True
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit: return False  #found cycle

            #cycle detection
            visit.add(i)
            for j in adj[i]:
                if j == prev:   #ignore parent node
                    continue
                if not dfs(j, i): #check for children
                    return False

        return dfs(0,-1) and n == len(visit)  #no cycle s + fully connected