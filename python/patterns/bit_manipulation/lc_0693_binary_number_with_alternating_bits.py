'''
693. Binary Number with Alternating Bits
time, memory 100, 83
'''


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        
        #shift by 1 place and do xor, 
        #must be 1 for all, if there are alternating bits
        x = n ^ (n >> 1 )   

        '''
        if all are 1 in x, then x + 1 has 1 followed by zeros. 
        1111 + 1 = 10000
        10000 & 1111 = 00000
        '''
        return (x & (x+1)) == 0   

