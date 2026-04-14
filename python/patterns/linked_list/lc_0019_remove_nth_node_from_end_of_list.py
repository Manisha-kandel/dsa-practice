'''
19. Remove Nth Node From End of List
15 minutes
''' 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #use concept of slow and fast pointers, instead of fast moving more steps, it simply starts from few nodes ahead but moves with same pace as slow. 
        #when fast reaches end, slow reaches the node to be deleted
        dummy = ListNode(0, head)      #dummy plays an important role
        slow, fast = dummy, head
        
        for i in range(n-1): #update fast
            fast = fast.next
        
        while fast and fast.next:   #move both together till fast reaches the end
            slow = slow.next
            fast = fast.next
        
        #now slow.next is the element to be removed
        slow.next = slow.next.next

        return dummy.next     #dummy plays an important role