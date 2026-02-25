'''
209. Minimum Size Subarray Sum
'''
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        l = 0
        currSum = 0
        res = float("inf")

        #r will stretch subarray
        for r in range(len(nums)):
            currSum += nums[r]
        
            #l will contract the subarray
            #we keep shrinking the subarray window as long as the condition holds
            while currSum >= target:
                res = min(res, r-l+1)    #res is updated only here
                currSum -= nums[l]
                l += 1
        
        return res if res != float("inf") else 0
                    

        