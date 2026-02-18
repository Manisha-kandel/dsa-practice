'''
424. Longest Repeating Character Replacement
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #keep maintaining hashmap for a sliding window
        # we keep track of the longest length, while moving
        
        counter = {}
        longest = 0

        l = 0
        for r in range(0, len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1

            while (r-l+1) - max(counter.values()) > k:     #window length - max value from counter dictionary
                l += 1
                counter[s[l]] -= 1
            
            longest = max(longest, r-l+1)
        
        return longest




#seemingly feeble change but much efficient: keeping track of maximum frequency (maxF)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #keep maintaining hashmap for a sliding window
        # we keep track of the longest length, while moving
        
        counter = {}
        longest = 0
        maxF = 0         #new

        l = 0
        for r in range(0, len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            maxF = max(counter[s[r]], maxF)       #new

            while (r-l+1) - maxF > k:   #window length - max frequency : new
                l += 1
                counter[s[l]] -= 1
            
            longest = max(longest, r-l+1)
        
        return longest









