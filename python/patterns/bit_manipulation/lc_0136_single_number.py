'''
136. Single number
time space beats 31, 25%
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #when we do xor, a number xor to itself is zero. 
        #so if we do xor for all elements in array, we can
        #get the number which is unique as the final answer. 
        res = 0

        for num in nums:
            res = res^num
        return res