'''
219. Contains Duplicate II
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        #use hashmap, just keep the last index of any number as it's value in the hashmap
        #compare with that index when a same value is found again, if the indices are in the asked interval, return True
        #else return FAlse after completing the  loop.
        hashmap = {}
        
        for i in range(len(nums)):
            n = nums[i]
            if n in hashmap:
                if (i - hashmap[n]) <= k:
                    # print(hashmap)
                    return True 
                else:
                    hashmap[n] = i    #no need to keep the earlier index, just keep the last known location/index of any number, compare with that one when next is found. 

            elif n not in hashmap:
                hashmap[n] = i    
                # print(hashmap)

        return False


'''Better soln by chatGPT: just my idea but better execution with less redundancy'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last = {}
        for i, x in enumerate(nums):
            if x in last and i - last[x] <= k:
                return True
            last[x] = i
        return False



'''
FAILED ATTEMPT: worked for some cases, but didn't work for large testcases.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        #maintain window of size k+1, and if there is any duplicate in there, return True, 
        #if you do all loops and end the process without finding any such, return False

        #try using window of k+1, a list from set, if length(window_list) < length(set): return True    
        
        if len(nums) <= 1:
            return False

        if k >= len(nums):
            numsSet = set(nums)
            return (len(numsSet) != len(nums))

        i = 0
        for i in range(len(nums)-k):
            window = nums[i:i+k+1]
            windowSet = set(window)
            if len(windowSet) < len(window):
                return True
            
        return False
        

'''