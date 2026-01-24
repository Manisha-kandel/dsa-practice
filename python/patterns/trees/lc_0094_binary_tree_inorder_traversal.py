'''
94. Binary Tree Inorder Traversal
time, memory beats 100%, 57%
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        inorder = []
        if not root:
            return inorder
        
        #left
        leftBranch = self.inorderTraversal(root.left)
        inorder.extend(leftBranch)
        #root
        inorder.append(root.val)
        #right
        rightBranch = self.inorderTraversal(root.right)
        inorder.extend(rightBranch)

        return inorder
