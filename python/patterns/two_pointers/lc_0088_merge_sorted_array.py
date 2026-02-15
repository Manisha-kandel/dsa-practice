'''
88. Merge Sorted Array
'''
#start filling appropriate numbers in nums1 from the last. Check the larger of the last pointers at two lists, insert in the kth position, decrement k pointer and the corresponding lists' pointer.  
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #we start keeping elements in correct position from the back

        i = m-1   #index of last(non-zero) element of nums1
        j = n-1
        k = m+n-1

        while j >=0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -=1


        


        