'''
461. Hamming distance
time, memory beats 100, 15%
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #counts of bits where value are different.
        #take xor of two, then count set bits.

        num = x^y
        cnt = 0
        while num > 0:
            cnt += num&1
            num = num >> 1
        return cnt