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