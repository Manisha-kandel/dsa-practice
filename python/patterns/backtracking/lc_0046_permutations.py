'''
46. Permutations
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #store the permutations in res, we know a permutation is complete when length of the path reach length of nums
        #to keep track of which elements are already used in permutations, use an array 'used'
        res = []                         # will store ALL permutations (final answer)
        used = [False] * len(nums)       # used[i] = True means nums[i] is already in current path
        path = []                        # current permutation we are building (changes during recursion)

        def backtrack():                 # helper that fills the next position in 'path'
            # BASE CASE: if path has same length as nums, we formed one full permutation
            if len(path) == len(nums):
                res.append(path[:])      # append a COPY of path (path[:] makes a new list)
                return                  # stop this branch and go back (backtrack)

            # TRY ALL CHOICES for the next slot in the permutation
            for i in range(len(nums)):
                if used[i]:              # if nums[i] already used in path, skip it
                    continue

                used[i] = True           # choose nums[i] (mark as used)
                path.append(nums[i])     # put nums[i] into the current permutation

                backtrack()              # recurse: fill the next slot

                path.pop()               # UNDO choice: remove last element (so we can try another number)
                used[i] = False          # UNDO choice: mark nums[i] as unused again

        backtrack()                      # start building permutations from empty path
        return res                       # return all collected permutations
