'''
122. Best Time to Buy and Sell Stock II
Did totally by myself in 15 minutes !!
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # print(prices)
        #dynamic programming concept as well
        profit = [0]*len(prices)
        last_buy = float("inf")
        sell = 0
        i = 0
        while i < len(prices):
            if i == 0:
                last_buy = prices[0]     #profit 0 for 1 day
                i += 1
                continue

            if prices[i] <= last_buy:
                while i < len(prices) and prices[i] <= last_buy:
                    last_buy = prices[i]
                    curr = 0
                    profit[i] = profit[i-1] + curr
                    i += 1

            if i < len(prices) and prices[i] > last_buy:
                curr = prices[i] - last_buy
                profit[i] = profit[i-1] + curr
                last_buy = prices[i]
                i += 1

        return profit[-1]

'''
pretty easy soln from revision
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #think of it as a graph, we need to find the rising part and keep adding that rise, that's all
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit += diff

        return profit