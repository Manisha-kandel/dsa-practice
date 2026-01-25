'''
191. Number of 1 Bits
time memory beats 100, 19%
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        #a point to note in bit manipulation, we don't need to explicitly convert number  to binary, when we give bitwise operators, it works on the binary version itself.  
        cnt = 0

        while n > 0:
            cnt += n&1         #n&1 gives 1 when LSB(Least Significant Bit) is 1, else 0.   
            n = n>>1           #right shift the number(binary) by 1, so that the second position (from last) is the next LSB. 
        return cnt
