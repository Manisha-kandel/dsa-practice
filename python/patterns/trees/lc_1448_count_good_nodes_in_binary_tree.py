'''
1448. Count Good Nodes in Binary Tree
15 minutes
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #when we are working at a node, we need to know what has been the largest number seen till reaching that node, if the node value >= largest seen till then (i.e. in the path), then it's a good node, else it's a bad node. 
        #helper fcn
        def dfs(node, maxVal):
            if not node: return 0

            res = 1 if node.val >= maxVal else 0   #good or bad? 
            maxVal = max(node.val, maxVal)         #update maxVal
            res += dfs(node.left, maxVal)          #do the count for left subtree
            res += dfs(node.right, maxVal)         #do the count for right subtree
            return res
        
        return dfs(root, root.val)   #count from root and downwards | could write float("-inf") as well, but root.val itself works