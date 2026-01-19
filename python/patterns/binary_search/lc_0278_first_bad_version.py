'''
278. First Bad Version
Time beats 88%, memory 81%
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        if n = 4:
        [1,1,1,1,0,0,0,0,0]
        can think of list(isBadVersion(n) for all n) to be a 
        sorted list in descending order, values being 1 and 0 only. 
        SAMPLE DATA: [False False True True True True] --> return 3 
                            as isBadVersion(3) is True but isBadVersion(2) is False. 
        '''

        if n <= 2:
            if isBadVersion(1):
                return 1
            else:
                return 2

        if isBadVersion(1):
            return 1
        else:
            i = 1 #if not(isBadVersion(1))     #to track False 
            j = n   #3 and more   #to track True
            while i<=j:
                if j-i == 1:
                    return j
                idx = (i + j) // 2
                if isBadVersion(idx) == False:
                    i = idx
                else:         #1
                    j = idx