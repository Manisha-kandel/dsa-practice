'''
128. Longest Consecutive Sequence
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #we create a set of nums, cause duplciate isn't needed for analysis
        #whenever we look at a number that hasn't been analysed for consecutive length(i.e. n-1 isn't in the set then it wasn't included in any length calculation), 
        #we start an analysis of it, basically while the next number keep coming, we keep adding the length, and when it stops, we record the length(basically comparing with max value yet obatined and keeping the larger one). 
        

        #create set: use numsSet and sort to create new nums for ease. 
        numsSet = set(nums)
        nums = list(numsSet)   
        nums = sorted(nums)    #sorted, no repitition 

        longest = 0

        i = 0
        while i < len(nums):     #while insted of for loop
            num = nums[i]

            #if a disjoint group starts, calculate it's length and update
            if num - 1 not in numsSet:
                length = 0

                while num + length in numsSet:
                    length += 1
                
                longest = max(length, longest)

                #update i for ease:    #while loop finishes faster
                i = i + length
        
        return longest
