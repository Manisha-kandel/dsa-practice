'''
153. Find Minimum in Rotated Sorted Array
time beats 100%
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        #keep maintaining a window that contains the least element. 
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1        #imp
            else:
                r = mid
        
        return nums[l]
