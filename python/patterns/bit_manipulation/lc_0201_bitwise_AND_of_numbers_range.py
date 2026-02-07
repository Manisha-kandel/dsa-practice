class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        shift = 0

        # Idea:
        # Bitwise AND of all numbers in [left, right] keeps only the
        # common left prefix of left and right.
        # As soon as a bit differs at some position, the AND over the range
        # will force that bit (and all lower bits) to 0.

        # Example:
        # left = 26  -> 11010
        # right = 30 -> 11110
        #
        # Shift right until both numbers are equal (find common prefix):
        # 26, 30 -> 13, 15 -> 6, 7 -> 3, 3
        #
        # Common prefix = 11 (binary)
        # Number of shifts = 3
        #
        # Shift back left by 3:
        # 11 << 3 = 11000 = 24

        # Find common prefix by shifting both numbers right
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1

        # Restore the prefix by shifting left
        return left << shift
