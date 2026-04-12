'''
450. Delete Node in a BST
25 minutes
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #deleting a node means, deleting the node's value, replace with an appropriate value 
        #and delete that value from it's original node, replace with appropriate value and 
        #keep doing it until we reach null (no nodes left for deletion)

        if not root: 
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:   #if there is no left tree, return right tree or null(if right is not there)
                return root.right
            elif not root.right: #there left but not right, return left or null
                return root.left
            
            #WHEN THERE ARE BOTH
            #find min in right subtree (the leftmost child of right tree)
            current = root.right

            while current.left:
                current= current.left
            root.val = current.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root

