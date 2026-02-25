'''
42. Trapping Rain Water
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #we keep track of what is the maximum height of the bar left(OR RIGHT (depending on which pointer is being used)) or equal to the position of the current index, then we see how much water could be held in that specific index with min(maxLeft, maxRight) - height[l(or r)]
        #Be mindful of the order of operations in the solution

        if not height:
            return 0
        
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]

        res = 0

        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
                # maxLeft = max(maxLeft, height[l])
                # l += 1
                # print(res, l, r)
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
                # maxRight = max(maxRight, height[r])
                # r -= 1
                # print(res, l, r)

        return res

