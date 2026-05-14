'''
752. Open the Lock, 15 minutes
'''
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        #BFS
        if "0000" in deadends: #starting point = deadend -> no sol
            return -1
        
        def children(lock):
            res = []
            for i in range(4):                          #for each digit, right turn and left turn
                digit = str((int(lock[i]) + 1) % 10)    #right turn
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10) #left turn
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        q = deque()
        q.append(["0000", 0])    #[lock, turns]
        visit = set(deadends)      #deadends are not option to explore, so keep in visit from beginning. 
        while q:                             #if lock is target, return; else continue BFS to get more children locks. 
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])
        
        return -1     #none found