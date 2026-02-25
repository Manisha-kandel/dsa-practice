'''
41. First Missing POsitive
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        #remove numbers(make them 0) greather than n, in the array nums
        for i in range(n):
            if nums[i] >= n or nums[i] < 0:
                nums[i] = 0

        #increase the indices by n, when corresponding number is found in the array     
        #indices start from 1 to n. (positive numbers)
        for j, num in enumerate(nums):
            num = num % n          #to get the already increased by n (or 2n, or 3n) values to what it originally was, we use the modulo operator.
            nums[num-1] = nums[num-1] + n
        
        #check for missing indices
        #that is the required first positive missing number. 
        for k, num in enumerate(nums):
            if num < n:
                return k+1

        #if the smallest is n, we reach the end of the array.
        return n



        
