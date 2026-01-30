'''
111. Minimum Depth of Binary Tree
DFS 
time, memory beats 22,33%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:     #if there is root but both left and right child are not there. 
            return 1

        res = 0

        if root.right and root.left:   #if there are both subtrees, use min of both
            res += 1 + min(self.minDepth(root.right), self.minDepth(root.left))
        elif root.right:       #if only right, have to take right
            res += self.minDepth(root.right) + 1
        else:                  #take left
            res += self.minDepth(root.left) + 1 

        return res


