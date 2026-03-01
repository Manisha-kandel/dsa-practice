class MinStack(object):
    '''
    we need to know the minimum of the stack, so we keep track of minimum till an index of stack in corresponding auxiliary stack called minStack. we return the minimum referring to the minStack, we return top from stack, we do push and pop in both of the stacks(stack & minStack) together.
    '''
    def __init__(self):  #initialize
        self.stack = []
        self.minStack = []

    def push(self, val):   #void
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        min_ = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(min_)

    def pop(self):   #void
        """
        :rtype: None
        """
        top = self.stack.pop()
        self.minStack.pop()
     
    def top(self): #return top element
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()