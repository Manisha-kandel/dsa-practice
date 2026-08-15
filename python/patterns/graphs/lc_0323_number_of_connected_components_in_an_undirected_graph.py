'''
323. Number of Connected Components in an Undirected Graph, 
'''
from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        '''
        UnionFind Logic: Start with res = n; for each edge, call union(n1, n2); 
        if roots differ (p1 != p2), merge based on rank, decrement res, and return 1; else return 0. 
        Use path compression (par[i]=par[par[i]]) in find() to flatten the tree for efficiency. 
        Result is total disjoint sets.
        '''
        
        #CREATE PAR AND RANK LISTS
        par = [i for i in range(n)]
        rank = [1] * n    

        #DEFINE FIND (TO FIND THE ULTIMATE PARENT)
        def find(n1):
            res = n1
            while res!= par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        #DEFINE UNION
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1==p2: return 0           #unsuccessful union

            if rank[p1]> rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1                     #successful union
        

        #FOR EACH EDGE, PERFORM UNION AND REDUCE THE #COMPONENTS BY 1 IF UNION WAS SUCCESSFUL
        res = n
        for n1,n2 in edges:
            res -= union(n1,n2)

        return res