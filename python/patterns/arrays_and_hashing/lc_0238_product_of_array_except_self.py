'''
238. Product of Array Except Self
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #one array to track prefix product
        #one to track suffix product
        #res will have prefix[i-1]*suffix[i+1] with edge cases of res[0] and res[n-1]
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        product = 1
        for i in range(n):
            product *= nums[i]
            prefix[i] = product
        # print(prefix)
        product_ = 1
        for i in range(n):
            product_ *= nums[n-1-i]
            suffix[n-1-i] = product_
        # print(suffix)
        res = [1]*n
        res[0] = suffix[1]
        res[n-1] = prefix[n-2]
        for i in range(1,n-1):
            # print(prefix[i-1])
            # print((n-1-i))
            # print(suffix[i+1])
            res[i] = prefix[i-1]*suffix[i+1]
        return res
