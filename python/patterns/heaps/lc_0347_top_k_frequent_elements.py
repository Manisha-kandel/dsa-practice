'''
347. Top K Frequent Elements
time, memory beats 30, 32%
'''

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        top_k = []
        heapq.heapify(top_k)
        for number in freq:
            # print(freq[number], number)
            heapq.heappush(top_k,(freq[number], number))
            if len(top_k) > k:
                heapq.heappop(top_k)
        
        # print(top_k)
        return [num for (f, num) in sorted(top_k, reverse=True)]       #return in correct order. 

        