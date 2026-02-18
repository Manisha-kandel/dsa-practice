'''
3. Longest Substring Without Repeating Characters
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we use slising window that preserves uniqueness of characters inside it
        #the length of the substring with unique characters are stored. 

        longest = 0
        charSet = set()

        l = 0
        r = 0
        for i in range(0, len(s)):

            length = 0
            while s[r + length] not in charSet:
                length += 1
                charSet.add(s[r+ length])
            
            # r = r + length - 1
            longest = max(longest, length)

        return longest