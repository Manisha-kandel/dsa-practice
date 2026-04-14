'''
143. Reorder List - 25 minutes
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #There will be first half and second half. If odd number of nodes are there, first half will have the additional element. | we use slow and fast pointers to do the work for deciding mid-point to split the linked list into two halves.
        #second half whould be reversed, then we will alternately keep elements from first half and reversed second half. That's how we get our results. 

        #find the splitting point (the middle)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the second half
        second = slow.next    #second half's head
        prev = slow.next = None  #first half's tail points to null, second half's prev is null

        while second:
            nxt = second.next   #store next node
            second.next = prev  #revert pointer
            prev = second       #update prev
            second = nxt        #update second
    
        #merge the halves
        first, second = head, prev   #prev reaches end of second while reversing, i.e. the head of reversed second half
        while second:         #    
            nxt1, nxt2 = first.next, second.next  #store next nodes
            first.next = second                   #point first to second
            second.next = nxt1                    #second to next of first
            first, second = nxt1, nxt2            #update both