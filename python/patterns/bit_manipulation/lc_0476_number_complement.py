'''
476. Number Complement
time, memory 100,12

'''
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bits = num.bit_length()
        mask = (1 << bits) - 1  
        
        '''
        5 -> 101
        bits = 3
        mask -> 1000 - 1 = 111
        5 ^ mask -> 101 ^ 111 -> 010
        '''
        return num ^ mask

        # print(bin(num))
        # print(bin(mask))
        # print(bin(num ^ mask))