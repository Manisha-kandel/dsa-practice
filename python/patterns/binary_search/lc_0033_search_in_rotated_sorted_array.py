'''
33. Search in Rotated Sorted Array
time, memory beats 100%, 28%
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #one half is always sorted when mid divides the array. 
        #can compare in the sorted hald: so, 
        #check if the target could be in the sorted half or not, 
        # update the search space accordingly
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            
            mid  = (l + r) // 2
                
            #if mid is the target
            if nums[mid] == target:    
                return mid
            #else, update pointers by comparing pointer to sorted half
            elif nums[l] <= nums[mid]:  #left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:                     #right half sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
