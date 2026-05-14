'''
1834. Single-Threaded CPU
20 mintues
'''
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #given [enqueueTime_i, processingTime_i]
        #at most one task at a time
        #idle OR do entirely the task with shortest processing time (tie broken with smallest index) 
        #can start a new one instantly, no cooldown period needed. 

        for i, t in enumerate(tasks):
            t.append(i)                 #[1,2,0]
        tasks.sort(key = lambda t: t[0])

        res, minHeap = [], []   #minimum processing time task is done first, so use minHeap
        i, time = 0, tasks[0][0]

        while minHeap or i < len(tasks):  #if all tasks done 
            while i < len(tasks) and time >= tasks[i][0]: #if enqueuetime reached, push to minHeap*
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1   #one less task* 

            if not minHeap:
                time = tasks[i][0]  #if enqueue time is not reached, jump to that time directly instead of incrementing one by one
            else:
                procTime, index = heapq.heappop(minHeap) #task to be done now  
                time += procTime   #time taken for task
                res.append(index)    #append index to res for record
        
        return res  