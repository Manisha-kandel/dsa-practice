'''
567. Permutation in String
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #concept of all the counts matching (starting from a to z) in a sliding window
        #here len(sliding window) == s1. 
        #we keep counter, then in every new step (new r value), we keep checking if matches == 26, 

        '''
        (my past bug): When updating matches in s2, treat the outgoing and incoming
        characters as TWO SEPARATE updates with clear "before/after" logic.

        Why? Because counts change by ±1 and matches should only change when a character flips:
            equal -> not equal  (matches -= 1)
            not equal -> equal  (matches += 1)

        If I try to update both pointers “together” or don’t isolate out/inn, I accidentally compare using
        the wrong state (already-mutated count), and edge cases break — especially when out == inn (same char
        leaves and enters the window). Always do:
            out = s2[l], inn = s2[r]
            update inn fully (adjust matches), then update out fully (adjust matches).
        '''


        if len(s2) < len(s1):
            return False
        
        #counts of both
        count1 = {}
        count2 = {}

        #initialize dicitonaries
        for i in range(ord('a'), ord('z')+1):
            count1[chr(i)] = 0
            count2[chr(i)] = 0
        
        #fill dictionary for s1
        for char in s1:
            count1[char] += 1

        #fill dictionary for s2
        for char in s2[:len(s1)]:
            count2[char] += 1

        Matches = 0
        for i in range(ord('a'), ord('z')+1):              #count matches for all characters
            if count1[chr(i)] == count2[chr(i)]:
                Matches += 1
        if Matches == 26:
            return True
        # print(Matches)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if Matches == 26:
                return True

            count2[s2[l]] -= 1          #these two lines were together and gave error on a testcase for a longtime. 
            if count2[s2[l]] + 1 == count1[s2[l]]:
                Matches -= 1
            elif count2[s2[l]] == count1[s2[l]]:
                Matches += 1

            count2[s2[r]] += 1         #these two lines were together and gave error on a testcase for a longtime. 
            if count2[s2[r]] - 1 == count1[s2[r]]:
                Matches -= 1
            elif count2[s2[r]] == count1[s2[r]]:
                Matches += 1
            l += 1



        print(Matches)
    
        return Matches == 26


        

  