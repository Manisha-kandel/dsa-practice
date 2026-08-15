#198. House Robber

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #hmm, so base caseshould be sth like
        n = len(nums)
        if n==0: return 0
        if n==1: return nums[0]
        if n==2: return max(nums[0], nums[1])

        maxRobPrev2 = nums[0]
        maxRobPrev = max(nums[0], nums[1])

        for i in range(2,n):
            maxRob = max(maxRobPrev, maxRobPrev2 + nums[i])
            maxRobPrev2 = maxRobPrev
            maxRobPrev = maxRob
        
        return maxRob