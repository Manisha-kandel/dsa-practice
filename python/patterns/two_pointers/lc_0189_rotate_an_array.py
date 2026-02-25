'''
189. Rotate an array
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)   #helps time if k > length of the array

        queue = deque(nums)
        i = 0
        while i < k:
            end = queue.pop()
            queue.appendleft(end)
            # print(queue)
            # print(list(queue))
            i += 1

        nums[:] = list(queue) 

        # res = list(queue)
        return nums
