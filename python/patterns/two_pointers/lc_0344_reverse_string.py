'''
344. Reverse String
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) -1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return s

#second solution: but this is not in place reversing.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for i in range(len(s)):
            stack.append(s[i])

        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
        return s