'''
767. Reorganize String
15 minutes
'''
class Solution:
    def reorganizeString(self, s: str) -> str:
        #
        count = Counter(s)   #hashmap, count each char
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:  #prev is sth ready to be inserted in future after some char, but since no intermediate chars available, the combination is not possible
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]

        return res