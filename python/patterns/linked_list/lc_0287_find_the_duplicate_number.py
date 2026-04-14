
'''
287. Find the Duplicate Number
15 minutes
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Step 1: detect if a cycle exists
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        #after slow and fast pointers meet, we move another slow2 pointer from head, and the current slow pointer from where it is, the point they intersect is the point where the cycle starts, i.e. the duplicate of the list. 
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow