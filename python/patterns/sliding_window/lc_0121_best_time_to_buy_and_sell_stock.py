'''
121. Best time to buy and sell stock
time beats 62%, memory beats 92%
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i, j = 0,1
        profit = 0
        while j < len(prices):  #last day we can sell is at the last entry
            buy = prices[i]                #7, 1, 1,1,
            sell = prices[j]                 #1,5,3,5
            if sell <= buy: 
                i = j                #1
                j = i + 1                #2
                continue
            else:                    # sell > buy
                gain = sell - buy                #4,2,6
                if gain > profit:
                    profit = gain                #4,6                         
                j = j + 1                #3   
        return profit

#REVISION
'''
121. Best time to buy and sell stock
time memory beats 20%ish
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        profit = 0

        while (j <= len(prices)-1) and (i <= len(prices)-1):
            sell = prices[j]
            buy = prices[i]
            if sell < buy: 
                i = j              #this is the core logic of update, stuck here for quite some time cause I did j = i + 1 instead of i = j
                j = j + 1
            else: # sell >= buy:
                gain = sell - buy
                profit = max(profit, gain)
                j = j + 1
        return profit

