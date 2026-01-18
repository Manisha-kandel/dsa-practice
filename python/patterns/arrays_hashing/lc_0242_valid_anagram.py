'''242. Valid Anagram'''

'''Solution 1: time - space beats 25%ish. '''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # hashmap_s = {}
        # hashmap_t = {}
        # print(sorted(s))
        # print(sorted(t))
        if sorted(s) == sorted(t):
            return True
        return False


'''Solution 2: time,space beats 50%, 10%'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq_diff = [0]*26
        for i in range(len(s)):
            idx = ord(s[i])-ord("a")
            freq_diff[idx] += 1
        # print(freq_diff)
        for i in range(len(t)):
            idx = ord(t[i])-ord("a")
            freq_diff[idx] -= 1
        # print(freq_diff)
        for i in range(26):
            if freq_diff[i] != 0:
                return False
        return True