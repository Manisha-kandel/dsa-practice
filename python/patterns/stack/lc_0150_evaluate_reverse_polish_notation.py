'''
150. Evaluate Reverse Polish Notation
'''
#ARRAY approach
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #we keep storing the numbers in a list as long as we keep seeing numbers
        #when we see an operand, we take the last two numbers and use that operators to the last two, and store that result as the last second of that array(update arr[-2] to this result of operation), remove the last element. (remove arr[-1])

        n = len(tokens)
        numbers = []
        operators = ['+', '-', '*','/']
        i = 0
        while i < n:
            num = tokens[i]
            if num not in operators:
                numbers.append(int(num))
                # print(numbers)
            else:
                op = num   #if it was in the operators, it was not a num
                if op == '+':
                    temp = numbers[-2] + numbers[-1]
                    # print(temp)
                elif op == '-':
                    temp = numbers[-2] - numbers[-1]
                    # print(temp)
                elif op == '/':        #stuck in this condition for sometime, truncating division towards zero.
                    a = numbers[-2]
                    b = numbers[-1]
                    temp = abs(a) // abs(b)
                    if a*b < 0:
                        temp = -temp
                    # print(temp)
                elif op == '*':
                    temp = numbers[-2] * numbers[-1]
                    # print(temp)
                numbers[-2] = temp
                # print(numbers)
                del numbers[-1]
                # print(numbers)
            i +=1

        return numbers[0]


#STACK
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        ops = {"+", "-", "*", "/"}

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                b = stack.pop()      #last element
                a = stack.pop()      #last second element
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:   # "/"
		    a = numbers[-2]
                    b = numbers[-1]
                    temp = abs(a) // abs(b)
		    if a*b<0:
			stack.append(-temp)
		    else:
			stack.append(temp)
        return stack[0]

