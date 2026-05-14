'''
210. Course Schedule II, 15 minutes
'''
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # 1. Build Adjacency List
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        output = []
        # visit: Courses added to output (Completed)
        # cycle: Courses in current DFS path (Detects infinite loops)
        visit, cycle = set(), set()
        
        def dfs(crs):
            # If crs in cycle, we found a loop (e.g., A needs B, B needs A)
            if crs in cycle:
                return False
            # If crs in visit, we already added this to 'output'. Skip to save time.
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            
            # --- THE KEY DIFFERENCE FROM COURSE SCHEDULE I ---
            # We use Post-Order Traversal: A course is "finished" only after 
            # all its requirements (pre) are processed and added to the output.
            cycle.remove(crs)        
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return [] # Return empty if any cycle is detected
        
        return output