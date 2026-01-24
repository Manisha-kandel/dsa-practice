'''
572. subtree of another tree
time, memory 32%, 7%: took 1 hour 13 minutes to do. 

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # will be a subtree if the same roots have same left subtree and same right subtree
        #Base cases could be: 
        #create isIdentical function to 
        #CHECK IF TWO NODES AND DESCENDANTS ARE IDENTICAL (I.E. SAME TREE FROM THERE)
        def isIdentical(root, subRoot):
            if not root and not subRoot:        #both none
                return True
            elif not root or not subRoot:       #else: one of them none 
                return False
            return (root.val == subRoot.val) and isIdentical(root.left, subRoot.left) and isIdentical(root.right, subRoot.right)

        #SEARCH LOOP FOR SUBTREE
        if not subRoot:        #none is a subtree 
            return True
        elif not root:       #else, if subroot is there but root is not, it's false 
            return False
        elif isIdentical(root, subRoot):
            return True      #if identical return true
        else:                #else do recursion to search further down
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


                