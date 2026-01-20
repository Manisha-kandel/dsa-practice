'''206. reverse linked list

time beats 100%, memory 7%
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            next_ = curr.next   #save the next value
            curr.next = prev    #reverse the pointer
            prev = curr
            curr = next_        #update prev and curr values   
        return prev      



        