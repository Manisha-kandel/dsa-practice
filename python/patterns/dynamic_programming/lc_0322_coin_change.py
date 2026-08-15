#322. Coin Change

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        bestCom = [amount+1]*(amount+1)
        if amount == 0: return 0
        #base cases
        bestCom[0] = 0
        
        #recurrence
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    bestCom[i] = min(bestCom[i-coin] + 1, bestCom[i])
                    # print(bestCom)

        if bestCom[amount] == amount+1: return -1
        return bestCom[amount] 
