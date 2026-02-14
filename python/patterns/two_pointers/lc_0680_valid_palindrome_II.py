'''
680. Valid Palindrome - II
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        while l < r:
            #when we find first mismatch, we should check if the remaining(by deleting left and right pointer elements) is palindrome or not. If none of them are palindrome then, return FALSE as deleting one element didn't give the palindrome expected.
            if s[l] != s[r]:
                skipLeft, skipRight = s[l+1: r + 1], s[l:r]  #range: l+1 to r ||  l to r-1
                return (skipLeft == skipLeft[::-1]) or (skipRight == skipRight[::-1])  #checking both with their reverses to check if any of them are palindrome
                
            l += 1
            r -= 1
        
        return True



#FAILED ATTEMPT: didn't work on some test cases.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1

        count_off = 0
        while i < j:
            if s[i] != s[j]:
                count_off += 1
                if count_off > 1:
                    return False
                #not move only one pointer
                if s[i+1] == s[j]:
                    i += 1
                elif s[i] == s[j-1]:
                    j -= 1
                continue
            i += 1
            j -= 1
        
        return True
'''