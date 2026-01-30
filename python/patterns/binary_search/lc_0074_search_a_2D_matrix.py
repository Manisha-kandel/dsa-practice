'''
74. Search a 2D matrix
time, memory beats 100,10
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #we have a m*n matrix, where values keep increasing in each col downwards and each row rightwards. 
        #can use maybe use (m+n) range, while that happens, do binary sort s.t. the index we want for an k in that range is [k//m][k%m]. 
        #continue binary search till we find the value, 
        #logic being if target is lower, go leftwards in the range (m+n), if target is higher, fo rightwards in the range(m+n)
        m, n = len(matrix), len(matrix[0])

        l,r = 0, m*n
        # for k in range(m*n):
        while l < r: 
            mid = (l+r)//2
            i = mid//n
            j = mid%n     #not mid%n - 1
            num = matrix[i][j]
            if target == num:
                return True
            elif target < num:
                r = mid
            else:
                l = mid + 1
                

        return False
        
        # print(num)
        # print(l,r,mid)
        # mid = (l+r)//2
        # print(num)
        # print(l,r,mid)
        # mid = (l)
        # print(m)
        # print(n)
        # print(k//n)
        # print(k%n - 1)
        # print(matrix[k//n][k%n - 1])