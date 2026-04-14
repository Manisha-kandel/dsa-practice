'''
92. Reverse Linked List II - 15 minutes
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #left <= right  | the positions start at 1 not 0. 
        #

        dummy = ListNode(0, head)
        
        #step 1: reach the node at position of left
        leftPrev, cur = dummy, head
        for i in range(left-1):
            leftPrev, cur = cur, cur.next

        #step 2: the required length from left (right-left + 1), keep reversing
        prev = None
        for i in range(right-left+1):
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        #update pointers: 
        leftPrev.next.next = cur  #point the tail of reversed to split right part
        leftPrev.next = prev      #point the split left part to head of reversed middle part
        return dummy.next