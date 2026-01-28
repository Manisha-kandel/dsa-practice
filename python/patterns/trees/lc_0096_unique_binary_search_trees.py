'''
96. Unique Binary Search Trees
time, memory beats 100, 16%
'''


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #this is catalan number problem, for n nodes there are c[n] many unique BST's
        c = [0] * (n  + 1)

        #base cases: 
        #for 0 node, 1 possible i.e. None, 
        #for 1 node, 1 possible

        c[0] = c[1] = 1

        for i in range(2, n+1):
            for j in range(0, i):
                c[i] += c[j] * c[i-j-1]

        return c[n]