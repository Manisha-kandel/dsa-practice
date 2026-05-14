'''
684. Redundant Connection, 20 minutes
'''
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        #return False if can't complete
        def union(n1, n2):              
            p1, p2 = find(n1), find(n2)

            if p1 == p2: return False          #there is a loop (both already share same parent)

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:           
            if not union(n1, n2):
                return [n1, n2]           #This is the redundant edge we are looking for ! 