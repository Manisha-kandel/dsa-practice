'''
14. Longest Common Prefix
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        n = len(strs)     #how many strings are there? 
        k = min(len(strs[i]) for i in range(n))    # number of characters in smallest string
        i = 0      #for strings
        j = 0      #for characters
        while j < k:
            for i in range(n):
                if strs[i][j] == strs[0][j]:   #check if all are equal to first character
                    continue
                else:                          #if not, return the prefix we have till now
                    return prefix
            prefix = prefix + strs[0][j]
            j = j + 1
                 
        return prefix