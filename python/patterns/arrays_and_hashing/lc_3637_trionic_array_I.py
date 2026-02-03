'''
3637: Trionic Array I
Time, memory beats 100,24%
'''
class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 4:                 #not possible with length less than 4
            return False
        if nums[1] < nums[0]:     #a base case
            return False
        
        p,q = 0, 0
        i = 0
        j = 1
        
        while j < n:
            if nums[i] == nums[j]:   #strictly inc or dec, never equal
                return False
            if p == 0:
                if nums[i] < nums[j]: 
                    pass
                else:
                    p = i
                i += 1
                j += 1
                # continue
            elif p and not q:
                if nums[i] > nums[j]:
                    pass
                else:
                    q = i
                i += 1
                j += 1
                # continue
            elif p and q:
                if nums[i] < nums[j]: 
                    i += 1
                    j += 1
                else:
                    return False
        if not p or not q:         #if we never reached p or q by the end of the array, return False 
            return False
        return True

