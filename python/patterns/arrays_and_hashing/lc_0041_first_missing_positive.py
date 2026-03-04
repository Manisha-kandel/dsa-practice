'''
41. First Missing Positive

Goal:
Find the smallest missing positive integer in O(n) time and O(1) extra space.

Key idea:
Use the array itself as a hash table.
Mark presence of values 1..n by adding a constant "base" to the index (value-1).

Important:
If we use modulo, DO NOT use % n because value == n would become 0.
Use base = n+1 for both:
- marking (add base)
- recovering original (num % base)
- checking (value < base means "not marked")
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        base = n + 1  # base used for marking + modulo + threshold checks

        # 1) Clean the array:
        # Replace invalid values (<=0 or >n) with 0 because we only care about 1..n.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0

        # 2) Mark presence:
        # For each value v in [1..n], add 'base' to nums[v-1].
        # We use v % base to recover the original value even if nums[i] was already increased.
        for num in nums:
            num = num % base        # recover original value in range [0..n]
            if num == 0:
                continue            # 0 means invalid originally, skip
            nums[num - 1] += base   # mark that 'num' exists

        # 3) Find the first index that was never marked:
        # If nums[i] < base, then (i+1) was never seen.
        for i in range(n):
            if nums[i] < base:
                return i + 1

        # 4) If all 1..n are present, answer is n+1.
        return n + 1



        
