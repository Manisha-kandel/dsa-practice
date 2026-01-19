'''
20. Valid Parenthesis
time beats 78%
memory beats 36%
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_pairs = {")": "(",
                         "}": "{", 
                        "]": "[" 
                         }
        open_brackets = ["(", "{", "["]
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == bracket_pairs[bracket]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False