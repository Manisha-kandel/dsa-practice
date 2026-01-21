'''217. Contains Duplicate'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums, if any twice, return true

        s_nums = sorted(nums)
        i,j = 0,1
        while j < len(s_nums):
            if s_nums[i] == s_nums[j]:
                return True
            i = i + 1
            j = j + 1
        return False

#REVISION
'''
217. Contains Duplicate
time, memory beats 70%,27%
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False
