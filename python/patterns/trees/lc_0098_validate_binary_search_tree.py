'''
98. Validate Binary Search Tree
10 minutes
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #helper recursive function
        def valid(node, left, right):          #if node is wrong itself, return False right away, else check left and right children as well and return if all are valid or not. 
            if not node: return True
            if not (node.val < right and node.val > left):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))