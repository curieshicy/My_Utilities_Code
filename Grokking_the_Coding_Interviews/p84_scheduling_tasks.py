import heapq
from collections import deque, defaultdict
def schedule_tasks(tasks, k):
    d = defaultdict(int)
    for task in tasks:
        d[task] += 1
        
    max_heap = []
    for task, freq in d.items():
        heapq.heappush(max_heap, (-freq, task))
    
    count = 0
    while max_heap:
        n = k + 1
        wait_list = []
        while n and max_heap:
            freq, task = heapq.heappop(max_heap)
            count += 1
            if freq < -1:
                wait_list.append((freq + 1, task))
                
            n -= 1
            
        for i in wait_list:
            heapq.heappush(max_heap, i)
            
        if max_heap:
            count += n
            
    return count
            
def main():
    print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))
main()
