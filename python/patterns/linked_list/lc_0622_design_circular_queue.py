#622. Design Circular Queue - 20 minutes
''''
We make a class ListNode for our convenience
How we approach this problem is: we decide left and right nodes (of class ListNode) to indicate the end bars of front and rear part. 
We keep inserting items in between them (right before self.right) when we are adding items to the queue. 
We take out the items next to self.left when we are doing the dequeue. 
We update those next and prev pointers accordingly, and update space on enqueue and dequeue. 
We keep track of how much of the space is remained (self.space), we update the remaining space count, when we enQueue or deQueue, we update the self.space accordingly. 
The steps 1 through 8 are given on how to think of the problem. 
'''
class ListNode:                                        #|1|
    def __init__(self, val, nxt, prev):
        self.val, self.next, self.prev = val, nxt, prev

class MyCircularQueue:

    def __init__(self, k: int):                        #|2|
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next= self.right

    def enQueue(self, value: int) -> bool:             #|7|
        if self.space == 0: return False
        cur = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = cur
        self.right.prev = cur
        self.space -= 1
        return True

    def deQueue(self) -> bool:                       #|8|
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True

    def Front(self) -> int:                          #|5|
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int:                           #|6|
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:                         #|3|
        return self.left.next == self.right

    def isFull(self) -> bool:                          #|4|
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()