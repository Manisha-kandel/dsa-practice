'''
75. Sort Colors
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #they are colored red, white or bluw. 
        #need to sort in place s.t. same colors are adjacent
        '''
        Red = 0
        white = 1
        blue = 2
        '''

        #let's use two pointers
        left = 0

        #keep all 0s in the from
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

        #keep all 1s after that
        left = left  #carry on from the last step
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        #since 0s and 1s are already in their places, 2 will be automatically sorted
        return nums

