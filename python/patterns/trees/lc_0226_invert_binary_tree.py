'''
226. Invert Binary Tree
Time beats 100%, space ~20%
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
	#base case
        if not root:
            return None
	#swap the immediate left and right nodes (nodes include the subtrees extending from them, not only the node values)
        root.left, root.right = root.right, root.left 
	
	#Recursion: apply the invertTree to each node
        self.invertTree(root.left)
        self.invertTree(root.right)
	
	#after the recursion is complete, return the root.
        return root

        
#REVISION
'''
226. Invert Binary Tree
time memory beats 100%, 16%
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root