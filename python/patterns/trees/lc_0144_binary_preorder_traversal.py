'''
144. Binary Preorder Traversal
time, memory beats 100%, 95%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #base cases
        preorder = []
        if not root:
            return preorder
        
        preorder.append(root.val)
        leftBranch = self.preorderTraversal(root.left)
        preorder.extend(leftBranch)
        rightBranch = self.preorderTraversal(root.right)
        preorder.extend(rightBranch)
        
        return preorder
        