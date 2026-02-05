'''
15. 3sum
time memory beats 96, 8%
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)

        #two sum logic: hashmap of number and target, create as we go, return the key value pair, if the value is found somewhere as we move along the nums.
        res = [] 

        #for 3sum == 0
        if nums[0] > 0:
            return res
        if nums[-1] < 0:
            return res
        
        n = len(nums)
        
        for i in range(0, n-2):  #go till index n-3
            # print(i)
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -(nums[i])
            l = i+1
            r = n-1
            # print(l)
            # print(r)
            # print(target)
            
            while l < r:
                if nums[l] + nums[r] > target:
                    r = r-1
                elif nums[l] + nums[r] < target:
                    l = l + 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -=1
                    while l < r and nums[l] == nums[l-1]: l += 1    #if this is repeating, triplet will be the same as just found, violates the condition
                    while l < r and nums[r] == nums[r+1]: r -= 1    #likewise
                    # l = r
                    # break
        return res



        
