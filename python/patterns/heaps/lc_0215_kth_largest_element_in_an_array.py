'''
215. Kth Largest Element in an Array
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #sth like maintain minHeap of size k
        minHeap = []
        heapq.heapify(minHeap)

        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k: 
                heapq.heappop(minHeap)
        
        return heapq.heappop(minHeap)