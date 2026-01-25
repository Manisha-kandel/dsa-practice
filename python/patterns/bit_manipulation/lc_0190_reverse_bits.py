'''
190. Reverse Bits
time, memory beats 60, 12
'''


class Solution:
    def reverseBits(self, n: int) -> int:    #e.g. 001
	''' 
	keep adding LSB from n to the res, left shift of res in every step allows place for the LSB, at the end we get reversed 	bits.
	'''
        res = 0
        for i in range(32):
            res = (res<<1) | (n&1)    #0 -> 00 + 1 = 01 --> 010 + 0 = 010 --> 0100 + 0 == 0100 (i.e. 100)
            n = n >> 1     # 001 -> 00 --> 0 
        return res