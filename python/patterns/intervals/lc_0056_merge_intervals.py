#56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        outputs = [intervals[0]]

        for start, end in intervals[1:]:
            if start > outputs[-1][1]:     #disjoint, simply append
                outputs.append([start, end])
            else:                          #overlap
                outputs[-1][1] = max(outputs[-1][1], end)
        
        return outputs