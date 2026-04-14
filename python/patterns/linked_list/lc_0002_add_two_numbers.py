'''
2. Add Two Numbers
15 minutes
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #the basic carryover and addition concept from childhood, but here we use property of linked list to navigate through the problem
        #the linked list is given in reversed order in each number such that the head is the one's place for the numbers, the next one is the tens place and so on
        #we keep adding from head, carrying over the 'carry' if any, then we keep adding the current positions' numbers from both the linked list and the carry. | we continue the process till we reach the end. 

        dummy = ListNode(0)   #for the result
        cur = dummy  

        carry = 0             #carry is 0 for ones' place
        while l1 or l2 or carry: 
            v1 = l1.val if l1 else 0   
            v2 = l2.val if l2 else 0

            #the new digit in result
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)     #new node in result

            #update pointers accordingly
            cur = cur.next  
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next    #return head of result which is dummy.next