#70. Climbing Stairs
#---------------------
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [0]*(n+1)
        ways[0] = 1
        ways[1] = 1

        for i in range(2, n+1):
            ways[i] = ways[i-1] + ways[i-2]

        return ways[n]
        

#-------------OR--------------------------------

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev_1 = 1
        prev_2 = 1

        if n==0 or n==1: return 1 

        for i in range(2, n+1):
            curr = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = curr

        return curr