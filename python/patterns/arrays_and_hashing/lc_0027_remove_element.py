'''
27. Remove Element
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)          #remember 'nums' keeps changing 
        while i < n:           #as long as index is within range of the array whose length is changing with val found inside it
            if nums[i] == val:
                # print(nums) 
                del nums[i]
                # print(nums)
                n = len(nums)  #no need to update i here, as after deleting that index, the next will come to the same position which should be checked later. 
            else:
                i = i + 1    #update by 1 only if current element is not in the index
            
        return len(nums)
        
        