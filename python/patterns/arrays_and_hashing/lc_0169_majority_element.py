'''
169. Majority Element
It maybe doable with heap as well. 
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        n = len(nums)

        if n == 1:
            return nums[0]

        for i in range(n):
            if nums[i] in counts:
                counts[nums[i]] += 1
                if counts[nums[i]] > n // 2:
                    return nums[i]
            else:
                counts[nums[i]] = 1

        
 
        