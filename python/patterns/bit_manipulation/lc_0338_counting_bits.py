'''
338. Counting Bits

'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        #we will try and use dynamic programming, 
        '''dp[n] = dp[n>>1] + bool(n&1)'''  
        dp = [0] * (n+1)  

        for i in range(1, n+1):  #0 to n
            dp[i] = dp[i>>1] + bool(i&1)     #binary add was happening or sth till I didn't do bool() and just did + i&1, int() took larger time than bool
        return dp
