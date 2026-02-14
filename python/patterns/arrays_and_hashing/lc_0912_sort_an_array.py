'''
912. Sort an array
'''
#BEST SOLUTION SINCE THE RANGE OF NUMBERS IN TESTCASES ARE LIMITED, USE HASHMAP TECHNIQUE RATEHR THAN QUICKSORT.
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minimum = min(nums)
        maximum = max(nums)
        
        #hashmap to keep count of numbers
        counts = {}
        #populating hash table 
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] +=1
            else:
                counts[nums[i]] = 1
            
        #ans
        ans = []
        for k in range(minimum, maximum+1):
            if k in counts:
                j = 0
                while j < counts[k]:
                    ans.append(k)
                    j +=1
        
        return ans



'''FAILED ATTEMPT(gave TLE for 2,2,2,2,2,2,2,2,..............):
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)     #void fcn with inplace sorting
        return nums 
        #we will use quicksort
        #choose an element as pivot (rightmost or random), swap with the rightmost element in the array to keep that as the pivot for the PARITIONing  --> do the partition (partitioning = keeping the pivot in it's final correct position but left and right halves aren't sorted yet) --> the Partition should return the index of the correct position of the pivot in the sorted array. 
        #call partitioning for left halves and right halves. 

    def quicksort(self, nums, left, right):
        if left >= right:         #0 or 1 elements = already sorted
            return
        random_index = random.randint(left,right)
        #swap rightmost and pivot elements to store pivot as rightmost element
        nums[right], nums[random_index] = nums[random_index], nums[right]
        pivot_index = self.partition(nums, left, right)
        self.quicksort(nums, left, pivot_index - 1)   #sort left part
        self.quicksort(nums, pivot_index + 1, right)  #sort right part
    
    def partition(self, nums, left, right):  #array, left index, right index
        pivot = nums[right]
        store = left
        # left, i = 0, 0    #i for traversing, left is the pointer which will ultimately poit th position where the pivot will be kept correctly after partitioning
        # while left < i:
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[store], nums[i] = nums[i], nums[store]  #swap left and i elements
                store +=1 
            i+=1
        
        #at last: swap left and right elements to get pivot in correct position
        nums[store], nums[right] = nums[right], nums[store]
        return store
'''



'''
A SOLUTION: 


from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return

        # pick pivot value (not necessarily at right)
        pivot = nums[random.randint(left, right)]

        # 3-way partition pointers
        lt = left          # nums[left : lt] < pivot
        pivot_index = left # current index scanning
        gt = right         # nums[gt+1 : right+1] > pivot

        while pivot_index <= gt:
            if nums[pivot_index] < pivot:
                nums[lt], nums[pivot_index] = nums[pivot_index], nums[lt]
                lt += 1
                pivot_index += 1
            elif nums[pivot_index] > pivot:
                nums[pivot_index], nums[gt] = nums[gt], nums[pivot_index]
                gt -= 1
            else:
                pivot_index += 1

        # Now:
        # left..lt-1  < pivot
        # lt..gt      == pivot
        # gt+1..right > pivot
        self.quicksort(nums, left, lt - 1)
        self.quicksort(nums, gt + 1, right)
'''




            
            


            

