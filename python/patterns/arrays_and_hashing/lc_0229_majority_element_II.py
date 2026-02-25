'''
229. Majority Element II
checked count.get(..., 0) syntax, did in 10 minutes
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        threshold = n//3
        count = {}              #track count
        res = []                
        for i in range(n):   
            if nums[i] not in res:    #if it's already appended in result, no need to do anything
                count[nums[i]] = count.get(nums[i], 0) + 1
                if count[nums[i]] > threshold:
                    res.append(nums[i])

        return res
        


        

