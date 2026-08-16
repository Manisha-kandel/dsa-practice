'''
57. Insert Interval - 10 minutes 
We compare the newInterval to each interval we have in the intervals list, 
3 conditions: 
a. disjointly before this interval, append/extend in order and return immediately. 
b. disjointly after this interval, append this interval, let newInterval be cause we don't know how later it will exactly fit. 
c. it overlaps, then update newInterval with merged one. 

We reach out of loop without returning if we never appended the newInterval (either as it is or modified along the way), so if for loop ends without returning res, append the newInterval to res, then return res. 
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:   #newInterval lies disjointly before the interval
                res.append(newInterval)        #append
                res.extend(intervals[i:])      #extend the rest
                return res                   
            elif newInterval[0] > interval[1]: #newInterval lies disjointly after the interval
                res.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

        res.append(newInterval)
        return res