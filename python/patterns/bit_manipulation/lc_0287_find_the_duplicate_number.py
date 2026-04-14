'''
287. Find the Duplicate Number
15 mintues
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        n = len(nums) - 1

        #iterate through each bit position (upto 17 for 10^5)
        for bit in range(18):
            mask = 1 << bit
            base_count = 0
            nums_count = 0

            for i in range(1, n + 1):
                if i & mask:
                    base_count += 1

            for num in nums:
                if num & mask:
                    nums_count += 1
            

            #if the bit appears more times than it should,
            #it's part of the duplicate number
            if nums_count > base_count:
                res |= mask
        
        return res