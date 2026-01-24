'''
232. Implement Queue using Stacks
time memory 100, 60
'''

from collections import deque

class MyQueue(object):

    def __init__(self):
        self.obj = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.obj.append(x)
        self.obj.rotate(1) #was rotation -1 for stack using queues

    def pop(self):
        """
        :rtype: int
        """
        return self.obj.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.obj[-1]   #

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.obj) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()