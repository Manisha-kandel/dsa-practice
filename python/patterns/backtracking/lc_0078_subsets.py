'''
78. Subsets
Basically, if we have reached leaf, add the subset to res, else 1.include this item -> do dfs(i+1) for next level | 2. exclude this item -> do dfs(i+1) for next level 
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):                 #modify res in place, return nth 
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])        #include ith element
            dfs(i+1)
            subset.pop()           #exlcude ith element
            dfs(i+1)
            
        dfs(0)                   #start with 0th element which will give all modifications
        return res     
