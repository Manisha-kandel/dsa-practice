#62. Unique Paths


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #state: dp[i,j] represents ways to reach upto that cell
        #recurrence: can come one way from cell above it, one way from cell left to it: so dp[i][j] = dp[i][j-1] + dp[i-1][j]
        #base case: dp[:][0] = 1's | dp[0][:] = 1's 
        #sentinel: no sentinel needed as every cell is reachable
        #guards: initializing first row and first col ensures, there is always valid range of cells we're looking at
        #hand-trace: 1,1,1,1,1,1,1,1 | 1,11--> rethought base case with this 

        #no need of whole grid, just last row and left cell --just for optimzization, not for now

        #initialize the dp grid with 0's
        dp=[[0]*n for i in range(m)]

        #base cases: populate first row and first col
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        #recurrence
        for i in range(1, m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        # print(dp)
        return dp[m-1][n-1]