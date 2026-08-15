#746. Min Cost Climbing Stairs
'''for the first time, too time taking for easy problem, but tricky was that, we calculate dp, but answer min of dp of past 2 things, so basically, we are paying for future 1 or 2 steps  extra in each entry of dp. so while answering, should look at past 2 dp's, whichever is small isthe answer'''

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #state: ans = min(dp[i-1], dp[i-2])
        #recurrence: dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        #base case: dp[0] = cost[0], dp[1] = cost[1]
        #sentinel: not needed, all cases possible, no placeholders needed in dp array
        #guards: none needed here
        #hand-trace: [10,15,20] --> [10,15,30,15]
        n = len(cost)
        dp = [float('inf')] * (n)

        #base cases
        if n==0: return 0
        if n==1: return cost[0]
        if n==2: return min(cost[0], cost[1])
        dp[0] = cost[0]
        dp[1] = cost[1]
        dp[2] = min(cost[0], cost[1]) + cost[2]

        #recurrence
        for i in range(3, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            # print(dp)
        
        return min(dp[-1], dp[-2])