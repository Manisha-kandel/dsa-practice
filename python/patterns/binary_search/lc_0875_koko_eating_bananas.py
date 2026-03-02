'''
875. Koko Eating Bananas
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        let's decide minimum and maximum speed to check for koko
        max = max(piles)  #pretty obvious
        min = 1 #my hunch was to do sum(piles)/ len(piles) as the minimum value but somehow it doesn't work. 
        '''
        res = max(piles)

        l, r = 1, max(piles)   #range of speeds to try
        while l <= r:          
            m = l + (r-l) // 2
            t = 0                        #time taken
            j = 0
            while j < len(piles):
                t += math.ceil(piles[j] / m) 
                j += 1
            
            print(t, l, m, r, res)

            if t <= h:            #if < h hours, check and update res
                res = min(res, m)
                r = m - 1         #we should check further lower speeds if they are still valie, i.e. m is needed lower, and hence r = r - 1
            else:                 #she can't eat all, so increase the m(by increasing l) and try. 
                l = m + 1       

        return res

