class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #one solution
        #not use the same element twice. 
        nums_sorted = sorted(nums)
        # print(nums_sorted)
        i = 0
        j = len(nums_sorted)  - 1
        while i < j:
            n1 = nums_sorted[i]
            n2 = nums_sorted[j]
            if n1 + n2 == target:
                # print(n1)
                # print(n2)
                idx1 = nums.index(n1)
                # print(idx1)
                if n1 == n2:
                    idx2 = nums.index(n2, (idx1 + 1))
                else:
                    idx2 = nums.index(n2)
                # print(idx2)
                return sorted([ idx1, idx2])
            elif n1 + n2 > target:
                j = j - 1
            else:
                i = i + 1

        return []
        