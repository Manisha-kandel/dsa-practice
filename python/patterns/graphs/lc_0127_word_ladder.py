
'''
127. Word Ladder, 20 minutes
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        '''
        nei = {
            "*ot": "hot", "dot", ..
            "h*t": "hit", ... and so on
            }
        '''

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        #BFS
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:       
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res        #found word -> return the res 
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:  #if it was already in visit, shorter length have been found for that word, so discard that in this step
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        
        return 0  #impossible to go from beingWord -> endWord, return 0