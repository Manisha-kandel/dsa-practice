class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        #simmple if-elif-else conditions and add/remove accordingly.
        
        stack = []

        if not operations:
            return 0

        for op in operations:
            if op == "C":
                stack.pop()

            elif op == "D":
                # new = stack[-1] * 2
                stack.append(stack[-1]*2)
            
            elif op == "+":
                stack.append(stack[-1]+stack[-2])
            
            else:
                stack.append(int(op))

        return sum(stack) if stack != [] else 0