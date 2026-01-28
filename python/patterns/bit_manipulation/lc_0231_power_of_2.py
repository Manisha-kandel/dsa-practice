'''
231. power of two
time, memory beats 100, 20%
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
	    ''' count set bits, if > 1 return False immediately, at the end return true if cnt == 1'''
        cnt = 0              #count of set bits
    
        while n > 0:
            cnt += n&1
            n = n >> 1
            
            if cnt > 1:
                return False
        
        return cnt == 1