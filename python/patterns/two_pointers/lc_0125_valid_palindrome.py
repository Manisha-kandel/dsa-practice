'''125. Valid Palindrome'''

'''Solution 1: time beats 47%, space beats 88%'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j = 0, len(s) -1

        while i <= j:
            if i == j:   #e.g: len 5, 3 = 3, then break the loop
                break
            if not(s[i].isalnum()):
                i += 1
            if not(s[j].isalnum()):
                j -= 1
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():    #if equal
                    i += 1
                    j -= 1
                else:
                    return False
        return True


#REVISION
'''
125. Valid Palindrome

Time, Memory beats 45%, 28%
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) -1 
        while i < j:      #when equal will be palindrome center and work anyway 
            if not(s[i].isalnum()):
                i = i + 1
                continue
            if not(s[j].isalnum()):
                j = j - 1
                continue
            if s[i].isalnum() and s[j].isalnum():
                if s[i] == s[j]:
                    i = i + 1
                    j = j - 1
                else:
                    return False
        
        return True

            
