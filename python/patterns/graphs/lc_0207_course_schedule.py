'''
207. Course Schedule, 20 minutes
'''
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #First, we map each course to prereq list
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        ## visitSet tracks nodes in the current recursion stack to detect cycles (back-edges)
        visitSet = set()

        ## Standard DFS approach to verify if the graph is a Directed Acyclic Graph (DAG)
        def dfs(crs):
            if crs in visitSet: return False      #if already is taken in same path and need to be taken again, it's a loop
            if preMap[crs] == []: return True     #if no prereq, course can be taken
            
            visitSet.add(crs)                     #add course
            for pre in preMap[crs]:
                if not dfs(pre): return False     #if prereq can't be taken, so can't the course itself
            
            # Backtrack: remove from current path so it can be visited via other paths
            visitSet.remove(crs)                  
            
            #Mark as "safe" by clearing prerequisites. This prevents redundant DFS calls on previously verified courses.
            preMap[crs] = []                      
            return True


        for crs in range(numCourses):             #check if all courses can be done or not
            if not dfs(crs): return False
        
        return True
