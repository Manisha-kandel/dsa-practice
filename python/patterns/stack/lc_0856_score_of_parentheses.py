'''
856. Score of Parentheses
time, memory beats 100,56
'''
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #given is a balanced parenthesis
        stack = [0]  # stack[-1] is the score of the current "frame"

        for ch in s:
            if ch == "(":
                stack.append(0)
            else:     # )
                v = stack.pop()
                to_add = 1 if v == 0 else v*2
                stack[-1] = stack[-1] + to_add
        return stack[0]

        

        
'''
another solution
'''
class Solution(object):
    def scoreOfParentheses(self, s):
        score = 0
        depth = 0

        for i, ch in enumerate(s):
            if ch == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    score += 1 << depth  # 2^depth

        return score