'''
543. Diameter of Binary Tree        
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #diameter can be sum of two lengths that are largest and nodes don't touch each other or sth
        #they may or may not pass through root. 
        
        # if not root.left and not root.right:
        #     return 0
        
        best = [0]

        def longest_path(node):
            if not node:
                return 0
            left_length = longest_path(node.left)
            right_length = longest_path(node.right)
            
            # print('left length: ' + str(left_length))
            # print('right length: ' + str(right_length))
            
            #store best dia found till now
            best[0] = max(best[0], left_length + right_length)
            #return longest length till the node
            return max(left_length, right_length) + 1

        longest_path(root)
        return best[0]

