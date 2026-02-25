'''
560. Subarray Sum Equals K

'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        we keep track of summation and their counts using hashmap. We keep updating summation (till the     index), and check if this summation - k is in the hashmap | if that is found, the count gives the number of subarrays that could give the k result | so update the result accordingly | move to next iteration and continue till end
        '''
        
        summation = 0
        prefix_sums = {0:1}        #this base initialization is important
        res = 0

        for i in range(len(nums)):
            summation += nums[i]
            diff = summation - k
            #first check the difference, then update. 
            #first check
            if diff in prefix_sums:   #if summation = 3 and target is 2, we check how many of prefix sum of 1 is there, and increment res by that. 
                res += prefix_sums[diff]

            #then update
            prefix_sums[summation] = prefix_sums.get(summation, 0) + 1

        return res
        


            

