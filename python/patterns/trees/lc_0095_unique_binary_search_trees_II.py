'''
95. Unique Binary Search Trees II

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        # for i, [start, i-1] go to right subtree
        # [i+1, end] go to left subtree
        # if size of tree == n, done
        #backtracking problem: we use for loop to take choices
        
        def generate(left, right):
            dp = {}
            #base cases
            if left == right: #range of length 1
                return [TreeNode(left)] 
            if left > right:
                return [None]
            if (left, right) in dp:
                return dp[(left, right)]

            res = []
            for val in range(left, right + 1):    #run for all possible values in the range
                for l in generate(left, val -1):  #for each possible node, create all possible left subtrees with the values left to the node
                    for r in generate(val + 1, right): # make all possible right subtrees
                        root = TreeNode(val, l, r)     #attach l,r pairs for each subtrees to the root node of the iteration
                        res.append(root)               #attach each unique trees (root, l,r) in the ultimate result list
            dp[(left, right)] = res               
            return res
        return generate(1,n)    #Initial range
        


        
        