'''
100. Is Same Tree
time memory beats 100%, 10%

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q:
            return False
        elif not p and q:
            return False
        elif p == None and q == None:        #kinda didn't quite understand how in recursion it plays out and works the answer but played by hunch and worked. 
            return True
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)     #core concept: if both left subtrees and right subtrees are equal, then only trees are same, got stuck here for long time. 
        