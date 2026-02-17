'''
304. Range Sum Query 2D - Immutable
'''
import numpy as np
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        '''
        THINK IN TERMS OF REGION, WHICH ARE ADDED, it's similar how you think in PIE(principle of inclusion exclusion) problems. 
	Remember that the prefix matrix has 1 extra row and col each, so think in terms of that new prefix matrix while using the arguments you get as row1, col1, row2, and col2. 
        Think in terms of PIE while creating prefix matrix, and while returning the sumRegion values.
        
	[[3, 0, 1, 4, 2], 
     	[5, 6, 3, 2, 1], 
     	[1, 2, 0, 1, 5], 
     	[4, 1, 0, 1, 7], 
     	[1, 0, 3, 0, 5]]


	[
	[0, 0, 0, 0, 0, 0], 
	[0, 3, 3, 4, 8, 10], 
	[0, 8, 14, 18, 24, 27], 
	[0, 9, 17, 21, 28, 36], 
	[0, 13, 22, 26, 34, 49], 
	[0, 14, 23, 30, 38, 58]
	]
	'''



        self.matrix = matrix
        # self.prefix = np.zeros_like(self.matrix)
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return

        rows, cols = len(matrix), len(matrix[0])

        # (rows+1) x (cols+1) so prefix[0][*] and prefix[*][0] are zeros
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self.prefix[i][j] = (
                    self.prefix[i - 1][j] +
                    self.prefix[i][j - 1] -
                    self.prefix[i - 1][j - 1] +
                    matrix[i - 1][j - 1]
                )
        # print(self.matrix)
        # print(self.prefix)

    def sumRegion(self, row1, col1, row2, col2):   #returns sum --> int
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        #
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (
            self.prefix[r2][c2]
            - self.prefix[r1 - 1][c2]
            - self.prefix[r2][c1 - 1]
            + self.prefix[r1 - 1][c1 - 1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)