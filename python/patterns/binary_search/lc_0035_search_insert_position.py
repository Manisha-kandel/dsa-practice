'''
35. Search Insert Position
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums)-1

        '''Binary search + target comparison with index | if found inside while loop return it  right away | if not, after while loop ends: compare to give the index '''

        while i < j:

            if nums[i] == target: 
                return i
            elif nums[j] == target:
                return j
            
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif  target > nums[mid]: 
                i = mid + 1
            else: 
                j = mid - 1

        #if no target is found, check with i, if target less than i, it should be in ith position, else in i+1 position

        if target <= nums[i]:      #less than or equal to: cause in single element case, while loop doesn't carry, so we need to return that
            return i 
        elif target > nums[i]:
            return i + 1
        # return i+1 #if we haven't found target yet, then i and j would go to the place, in between of them will be inserted the target (i.e. jth index)