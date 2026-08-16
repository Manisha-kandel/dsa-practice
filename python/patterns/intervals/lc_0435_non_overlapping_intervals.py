#435. Non-overlapping Intervals - 15 minutes
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #
        intervals.sort()            #sorted by start, then end | this sorting helps in the for loop logic as well

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]: 
            if start >= prevEnd:           #if this one is disjointly after previous interval
                prevEnd = end              #update the prevEnd for future comparisions
            else:                          #else, it's overlapping in some form to the last, then we delete(abstractly) the interval with later end point to minimize the number of intervals to be deleted, so update the prevEnd to be that of the min of these 2 as the max is deleted.  
                res += 1 
                prevEnd = min (end, prevEnd)
        
        return res