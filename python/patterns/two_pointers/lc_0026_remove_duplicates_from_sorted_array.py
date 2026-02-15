'''
26. Remove Duplicates from Sorted Array
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #j will keep track of unique elements
        #i passes through all the elements in the array
        j = 0
        i = 0
        while i < len(nums):
            if nums[i] != nums[j]:   #if a new element is found, increment j and keep that in nums[j]
                j += 1
                nums[j] = nums[i]
            i += 1

        return j+1    #return index + 1 --> size of unique elements 