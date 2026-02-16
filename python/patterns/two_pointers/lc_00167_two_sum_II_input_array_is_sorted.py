'''
167. Two Sum II - Input Array Is Sorted
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #the numbers is in non-decreasing order: 2,3,3,4,8,9
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] < target:   #move i to right
                i += 1
            elif numbers[i] + numbers[j] > target: #move j to left
                j -= 1
            else:
                return [i+1, j+1]       #if found, return the pair (indexing starts from 1 for return indexes, so add 1 to each)
         
        return []      #return [] if none pair is found