'''
342. Power of 4
time, memory beats 100, 35%
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        '''similar logic to power of two, instead of 1,
        we right shift by 2 while counting cause:
        4^0 = 1   | 00001  | true
        4^1 = 4   | 00100  |true
        4^2 = 16  | 10000  |true
        6 | 110 | false
        3 | 11 | false
        and so on. 
        '''
	# the function should return true if there are no set bits (1 bits) at odd position and, there is only 1 set bit in even position. 
        
        cnt = 0
        while n > 0:
            cnt += n&1
            if (n >> 1)&1 == 1:   #if the odd positions have 1, then return 0. 
                return False
            n = n >> 2            #move to another even position
            if cnt > 1:     
                return False
        
        return cnt == 1

