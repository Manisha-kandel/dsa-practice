'''
703. Kth Largest Element in a Stream
time, memory beats 95, 27%
'''

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:     #takes out the least in first pop, second and till n-k smallest. At the EOL, the min heap has k largest elements 
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)        #add the elements
        if len(self.heap) > self.k:           #pop one if inserting this exceeded the desired min heap size
            heapq.heappop(self.heap)

        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)