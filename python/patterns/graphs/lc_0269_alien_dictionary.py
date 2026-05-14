'''
269. Alien Dictionary
'''
from typing import List

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Initialize graph with every unique character
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            
            # Prefix check: invalid if longer word precedes its own prefix
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) # Directed edge: char1 -> char2
                    break

        visit = {} # False=Visited, True=Current Path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c] # Return visit state

            visit[c] = True # Mark visiting (path)
            # Sort neighbors for smallest lexicographical order
            for nbr in sorted(adj[c], reverse=True):
                if dfs(nbr):
                    return True # Cycle detected
            
            visit[c] = False # Mark visited (safe)
            res.append(c) # Post-order collection
            return False

        # Process keys in reverse to assist alphabetical requirement
        for c in sorted(adj.keys(), reverse=True):
            if dfs(c):
                return "" # Found invalid cycle
        
        # Reverse post-order for correct topological sequence
        return "".join(res[::-1])