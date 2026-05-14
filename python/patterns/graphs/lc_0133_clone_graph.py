#133. Clone Graph, 15 minutes
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        #return deep copy of the graph
        #we need to clone nodes and connect cloned nodes to the clones of it's neighbors. 
        #for each class Node: there is val and neighbors
        oldToNew = {}

        def dfs(node):       #return copy of node, by looking up if already present, else by creating copy
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)       #makes node with self.val = val, and neighbors = [] 
            oldToNew[node] = copy       #write in hashmap
            for nbr in node.neighbors: #assign neighbors
                copy.neighbors.append(dfs(nbr))  #dfs returns copy of the node

            return copy           

        return dfs(node) if node else None  