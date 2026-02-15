'''
1768. Merge Strings Alternately
'''
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0
        word = ""
        #while both of them have valid indices keep adding alternately
        while i < len(word1) and j < len(word2):
            word += word1[i]
            word += word2[j]

            i +=1
            j +=1
        

        #while loop exited means either word1 or word2 has remaining parts, append the remaining part at the end of the word
        if i < len(word1):
            word += word1[i:]
        else:
            word += word2[j:]

        return word