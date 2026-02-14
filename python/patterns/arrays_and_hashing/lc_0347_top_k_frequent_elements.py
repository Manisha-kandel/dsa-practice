'''
347. top k frequent elements
'''
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1) Build hashmap for counts
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1          
            else:
                freq[num] = 1           

        # 2) Min-heap that stores only the current best k candidates
        #    Each heap item is (frequency, number)
        top_k = []
        heapq.heapify(top_k)            # optional here; [] is already a valid heap

        # 3) Push each unique number into heap, keep heap size <= k
        for number in freq:
            heapq.heappush(top_k, (freq[number], number))  # push (count, value)

            # If heap grew beyond k, remove the smallest frequency item
            # This way, heap always contains the k most frequent numbers seen so far
            if len(top_k) > k:
                heapq.heappop(top_k)

        # 4) Heap has k items but not necessarily sorted in output order
        #    Sort descending by frequency, then extract just the numbers
        return [num for (f, num) in sorted(top_k, reverse=True)]
