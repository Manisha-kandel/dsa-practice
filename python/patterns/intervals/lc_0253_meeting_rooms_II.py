#253. Meeting Rooms II - 15 minutes

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):   
            if start[s] < end[e]:   #we reach a time to start a meeting (just use < cause if s==e, then we end meeting first then start)
                s += 1
                count += 1
            else:                   #we reach a time when a meeting is ending
                e += 1
                count -= 1
            res = max(res, count)
        return res
            