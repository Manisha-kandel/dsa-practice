'''
199. Binary Tree Right Side View 
10 minutes
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #right side view means, for each level, we see the last element in the queue when we do a BFS using queue
        #we use the concept to come to a solution 

        if not root: return []

        res = []
        q = deque([root])

        while q:   
            n = len(q)          # how many elements are in this level of tree
            for i in range(n):  #for each element, take it out, and append it's children to the q. 
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
                #if it's last element of the level, append to res.
                if i == n-1: res.append(node.val) 
            
        return res
