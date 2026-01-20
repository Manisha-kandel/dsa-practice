'''21. Merge two linked lists
Time and memory taken not good, try in-place in future. 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        dummy = ListNode(0)              #create dummy node 
        tail = dummy                     #tail will be used to expand this new list

        while l1 and l2:
            if l1.val <= l2.val:
                nxt = l1.next                 #store the next value so as not to lose it
                tail.next = l1             #attach the head node of l1 (simple pointed as l1) it to the new list as it's tail
                l1 = nxt                   #update l1 as the remaining of the list using the stored next value
                tail = tail.next           #update tail
                print(dummy)
            else:
                nxt = l2.next              #same process for l2
                tail.next = l2
                l2 = nxt
                tail = tail.next
        tail.next = l1 if l1 else l2      #attach remaining parts
                                          #no need to check when both are None, cause during last comparison, one list has at least one node remaining. 
        return dummy.next
        
        