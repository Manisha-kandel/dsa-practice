'''
69. Sqrt(x)
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        #we use binary search for this one, we iterate from 1 through n, we keep dividing our valid space into halves until we find the solution. 


        l, r = 0, x        #     
        while l <= r:
            m = l + (r-l)//2
            # print(m)
            sq = m**2
            if sq < x:
                l = m +1
                print(m,l,r)
            elif sq > x:
                r = m - 1
                print(m,l,r)
            elif sq == x:
                return m 
        return r         #I was returning l for a long time, grave mistake ! Since, r is decremented by 1 already in the elif condition, returning r gives the exact value needed. | always practice an example in paper. 
        


