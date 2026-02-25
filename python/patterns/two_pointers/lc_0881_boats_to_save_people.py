'''
881. Boats to Save People
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''at most two people means we can use l and r pointer to see if those 2 fit together or not.'''
        people = sorted(people)
        # print(people)
        l, r = 0, len(people) - 1
        res = 0
        while l <= r:
            left, right = people[l], people[r]
            if l == r:
                res += 1
                break

            if left + right <= limit:
                res += 1
                l += 1
                r -= 1
            else:
                if right <= limit:
                    res += 1
                    r -= 1
                else:   #left at last
                    res += 1
                    l += 1
        
        return res

                




