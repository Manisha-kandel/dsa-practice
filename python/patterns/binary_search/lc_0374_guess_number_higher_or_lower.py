'''
374. Guess Number Higher or Lower
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #guess returns 0, 1 or -1 based on whether the number guessed is equal, higher or lower. 

        l, r = 1, n

        while l <= r:
            m = (l + r)//2 #l + (r-l)//2
            # print(m, l, r)
            if guess(m) == 0:
                return m
            elif guess(m) < 0:
                r = m-1
                # print(m, l,r)
            else:
                l = m + 1
                # print(m,l,r)
        
        return l
        


        