'''141. Linked List Cycle
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #will use fast and slow pointers concept (two pointers)
        fast, slow = head, head
        while fast and fast.next:    #if fast.next is NOne, cycle breaks
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False             #cycle breaks means fast.next points to None, the end of the linked list, i.e. there is no loop