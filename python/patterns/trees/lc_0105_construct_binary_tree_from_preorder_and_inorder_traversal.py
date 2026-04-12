'''
105. Construct Binary Tree from Preorder and Inorder Traversal
15 minutes
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #the concept is at each step, the first of the preorder is root, and all the elements left of that root in inorder are of left tree and those in right are of right subtree.
        #we use the concept to come to a solution

        #edge cases
        if not preorder or not inorder: return None

        root = TreeNode(preorder[0])
        node_index = inorder.index(preorder[0])
        # print(node_index)
        root.left = self.buildTree(preorder[1: node_index+1], inorder[:node_index] )   #Preorder: first is root, next node_index many are from left tree
        root.right = self.buildTree(preorder[node_index+1:] , inorder[node_index+1:])  #Inorder: node_index has root, right to it belongs to right tree

        return root