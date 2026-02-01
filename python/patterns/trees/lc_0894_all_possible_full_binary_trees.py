'''
894. All Possible Full Binary Trees
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        #full binary tree always has odd number of nodes, root(1) + left subtree(odd) + right subtree(odd)
        if n%2 == 0:
            return [] 
        
        if n == 1:
            return [TreeNode(0)]
        
        # root = TreeNode()
        treesFBT = []
        for i in range(1, n-1, 2):  #1,3,5,...n-2
            for L in self.allPossibleFBT(i):      #all left subtrees
                for R in self.allPossibleFBT((n-1)-i):   #all right subtrees, important to run in loop right in the recursion call (probably, not sure)
                    root = TreeNode(0)
                    root.left = L
                    root.right = R
                    treesFBT.append(root)
        
        return treesFBT
        
        