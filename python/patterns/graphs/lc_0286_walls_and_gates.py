'''
286. Walls and Gates
'''
from typing import (
    List, collections
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        #this solution will use MULTI-SOURCE BFS using a visit set. 
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = collections.deque()

        def addRoom(r,c):               #add room to the queue 
            if (r < 0 or r == ROWS or c < 0 or c == COLS or \
                (r,c) in visit or rooms[r][c] == -1): #1.outside grid, 2.already visited, or 3. is a wall
                return
            visit.add((r,c))   
            q.append([r,c])
        
        #add the gates to the queue and visit set. 
        for r in range(ROWS):      
            for c in range(COLS):
                if rooms[r][c] == 0:    #add gates to visit and queue
                    q.append([r,c])
                    visit.add((r,c))
        
        #gates are at dist 0.
        dist = 0
        #Initially, we are at gates(queue has gates now) and dist = 0 
        #-> we do multi-source BFS: for each level, we assign rooms with distance(rooms[r][c] = dist), 
        #-> we add rooms in new layer of BFS to visit with dfs fcn: addRoom, 
        #-> then we add to distance(dist += 1) corresponding to those rooms in queue
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist+= 1