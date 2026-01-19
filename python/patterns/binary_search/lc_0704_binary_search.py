'''
704. Binary Search
time beats 100%, 
memory beats 36%
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        nums -> sorted in ascending order
        target -> exists return the index, else -1. 
        sorted means we can check mid index, move to appropriate half's mid index 
        based on value is greater or smaller, and so on like that. 
        i = 0
        j = len(nums)-1
        idx = (i + j) //2
        '''
        if len(nums) == 0:
            return -1
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        i = 0
        j = len(nums)-1
        idx = (i + j) //2
        num = nums[idx]
        while i <= j:
            if num == target:
                return idx
            elif num < target:
                i = idx + 1
            else:
                j = idx - 1
            idx = (i + j) //2
            num = nums[idx]
        return -1