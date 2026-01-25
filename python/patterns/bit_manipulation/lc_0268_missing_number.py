'''
268. Missing Number
time, memory beats 62, 15%
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #we will use all numbers from 0 thru n
        #do xor operation among all num of 'nums' and all numbers in the range 0 to n
        res = 0
        for i in range(0, len(nums)+1):
            res = res^i
        for num in nums:
            res = res^num           #if 0 is repeating, we will still have res as 0 to return, so no extra need of base case, the missing value is found by default with xor. 
        return res 

