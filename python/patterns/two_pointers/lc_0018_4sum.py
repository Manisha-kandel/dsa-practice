'''
18. 4Sum
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)  #since it's asking for numbers and not indexes, sorting is okay
        n = len(nums) 
        #[1,0,-1,0,-2,2] -> nums
        #[-2,-1,0,0,1,2] -> sorted nums

        #skipping duplicates for k, l, i and j is important
        for k in range(0, n - 3):
            # skip duplicate k
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            for l in range(k + 1, n - 2):
                # skip duplicate l
                if l > k + 1 and nums[l] == nums[l - 1]:
                    continue

                i = l + 1
                j = n - 1
                #never set target = target - .... 
                need = target - nums[k] - nums[l]

                while i < j:
                    curr = nums[i] + nums[j]

                    if curr < need:
                        i += 1
                    elif curr > need:
                        j -= 1
                    else:
                        res.append([nums[k], nums[l], nums[i], nums[j]])

                        i += 1
                        j -= 1

                        # skip duplicates for i
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1

                        # skip duplicates for j
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1
        return res


