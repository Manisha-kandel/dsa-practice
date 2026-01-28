'''
22. Generate Parentheses
time, memory 100, 18
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #we can add open parenthesis only if open < n
        #can add closing only if closed < open
        #valid if open == closed == n
        stack = []
        res = []

        def backtrack(nopen, nclosed):
            if nopen == nclosed == n:
                res.append("".join(stack))
                return
            
            if nopen < n:
                stack.append("(")
                backtrack(nopen + 1, nclosed)
                stack.pop()  #**important part of backtracking: undoing current choice to continue to next**
            
            if nclosed < nopen:
                stack.append(")")
                backtrack(nopen, nclosed + 1)
                stack.pop()  #**

        backtrack(0,0)   #call backtrack for solving
        return res


        #EXTRA
        #ways to form n pairs of parenthesis = nth catalan number
        #base cases
        # dp = [0] * (n+1)   
        # dp[0] = dp [1] = 1

        # for i in range(2,n+1):     #2 to n
        #     for j in range(0,n):   #1 to n-1 
        #         dp[i] += dp[j]*dp[n-j-1]   
        
        # return dp[n]
        
        