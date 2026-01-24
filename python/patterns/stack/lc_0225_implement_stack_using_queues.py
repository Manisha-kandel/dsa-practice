'''
225. Implement Stack using Queues
time, memory 100, 25
'''

from collections import deque
class MyStack(object):

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        # if len(self.stack) > 1:
        self.stack.rotate(-(len(self.stack)-1))   #notice how rotation is by '-(len - 1)', the + direction gave error for a long time
	''' or a much simpler solution
	self.stack.rotate(1)
	'''

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()