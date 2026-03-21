'''
1046. Last Stone Weight
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #given stones
        #heaviest two bang each other, destroying part or all of it, heap is used cause "heaviest two" comes into play
        
        maxHeap = [-wt for wt in stones]
        heapq.heapify(maxHeap)

        if len(maxHeap) == 1: return -(maxHeap[0])

        while maxHeap:
            first = heapq.heappop(maxHeap)
            if maxHeap: 
                second = heapq.heappop(maxHeap)
                if first == second: continue
                else: heapq.heappush(maxHeap, first-second)
            else: return -(first)

        return 0
