'''
701. Insert into a Binary Search Tree 
5 minutes
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #we will find a correct parent and left or right position for the val to be inserted. 
        #one base case, 
        #and recursion (two if conditions for left and right part each), that's it. 
        if not root: return TreeNode(val)

        if val > root.val: 
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val: 
            root.left = self.insertIntoBST(root.left, val)

        return root