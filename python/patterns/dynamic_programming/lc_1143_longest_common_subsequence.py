#1143. Longest Common Subsequence

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #state: it's a 2d DP, longest common subsequence length till now 
        #recurrence: 1. if the current letters are equal, this cell = (topleft cell + 1)
                    #2. if not equal, then max of (top, left) 
        #base cases: dp[0][0] = (text1[0]==text2[0])
        #sentinel: none required
        #guards: within the grid (if either i or j is -1, value is 0 for that): for thiswe can add first row and first col just like that as 0, then simple recurrence formula would make sense
        #hand-check: done
        '''    "" a  b  c  d  e
            --------------------
           ""| 0  0  0  0  0  0
            a| 0  1↖ 1  1  1  1
            c| 0  1  1  2↖ 2  2
            e| 0  1  1  2  2  3↖
        '''

        #initialization
        m = len(text2)
        n = len(text1)
        dp = [[0]*(n+1) for i in range(m+1)]
        # print(dp) #correct

        dp[1][1] = (text1[0] == text2[0])
        # print(dp)

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]