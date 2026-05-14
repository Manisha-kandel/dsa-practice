'''
621. Task Scheduler
20 minutes
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #each time, idle or one task can be done. Can be done in any order, but n-gap between two tasks with the same label, return minimum time taken (CPU intervals) to complete all tasks.
        '''
        Basically, here we use maxHeap cause the most frequent work should be done first to ensure the least idle time | our maxHeap is basically the store of all work that we can do at this point of time (with every time stamp, maxHeap is updated based on available works in queue). 
        Another point to keep in mind is, because of the idle time, there is a certain time we have to wait before we keep that task in the maxHeap, that's why queue leverages (-unit of task remaining, time it will be available to be done)
        We run the while loop even though until all tasks are done (i.e. none in maxHeap(can be done immediately) none in queue(waiting to be entered to maxHeap)). 
        '''


        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]  #the frequency of tasks matter, not the keys. 
        heapq.heapify(maxHeap)

        time = 0
        q = deque()   #this will have the [-cnt, availableTime] pairs. 

        while maxHeap or q:    #run the while loop even though until all tasks are done
            time += 1

            if maxHeap: 
                cnt = 1 + heapq.heappop(maxHeap)    #reduce one task unit
                if cnt:
                    q.append([cnt, time + n])       #when will this task be next available to be kept on heap? time + n
            
            if q and q[0][1] == time: 
                heapq.heappush(maxHeap, q.popleft()[0])  #check if at this time stamp new work is available to be done (i.e. to be moved to maxHeap)
            
        return time