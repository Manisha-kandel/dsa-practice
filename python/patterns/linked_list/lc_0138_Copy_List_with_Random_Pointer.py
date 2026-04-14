#138. Copy List with Random Pointer - 10 minutes
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Give answer in 2 pass: first copy the nodes with values itself using the hasmap
        #in second pass: assign the pointers of the independent nodes(in the hashmap) to the copies of next and random pointers of the original linked list using origToCopy hashmap.  
        origToCopy = {None: None}

        #orig to copy hashmap of nodes with new nodes, but with values only
        cur = head
        while cur: 
            copy = Node(cur.val)
            origToCopy[cur] = copy
            cur = cur.next

        #assigning those copy nodes in hashmap with .next and .random, using the copies and hashmap
        cur = head
        while cur:
            copy = origToCopy[cur]
            copy.next = origToCopy[cur.next]
            copy.random = origToCopy[cur.random]
            cur = cur.next

        return  origToCopy[head]