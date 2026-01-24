'''
145. Binary Tree Postorder Traversal
time, memory beats 100%, 89%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        postorder = []

        if not root:
            return postorder
        #left
        leftBranch = self.postorderTraversal(root.left)
        postorder.extend(leftBranch)
        #right
        rightBranch = self.postorderTraversal(root.right)
        postorder.extend(rightBranch)
        #root
        postorder.append(root.val)

        return postorder
        
