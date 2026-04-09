'''
973. K Closest Points to Origin
10 minutes, did myself, yay !! 
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #looks like create a min heap using the distance from the origin (i.e. x**2 + y**2) and return all elements in the heap. We use negative of distances to maintain minHeap s.t. when we pop the minimum number, the -(largest distance in the heap) is popped off, and the ones we need are still in the heap.  
        minHeap = []
        heapq.heapify(minHeap)

        for [i,j] in points:
            heapq.heappush(minHeap, [-(i**2 + j**2), i, j] )   #ordered by first element

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return list([i,j] for [d, i, j] in minHeap) 