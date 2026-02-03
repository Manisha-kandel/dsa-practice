'''
49. Group Anagrams
time, memory beats 20,50%
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #should have a 
        letters = dict()

        # print(str(sorted(strs[0]))

        for string in strs: 
            key = str(sorted(string))
            print(key)
            if key in letters:
                letters[key].append(string)
            else:
                letters[key] = [string]
        # print(letters)
        # print(sorted(strs[0]))
        return letters.values()