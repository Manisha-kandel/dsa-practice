'''
11. Container With Most Water
time memory beats 91, 5%

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l = l + 1
            elif height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1
                r = r - 1

        return max_area