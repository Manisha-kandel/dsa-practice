'''
1929. Concatenation of Array
'''

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        ans = nums
        ans.extend(nums[:])
        return ans