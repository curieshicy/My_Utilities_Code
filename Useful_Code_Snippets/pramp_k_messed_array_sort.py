'''
           0  1  2  3  4  5  6  7  8   9
    arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9] k = 2
                           i           i
'''
import heapq
def sort_k_messed_array(arr, k):
    heap = [i for i in arr[:k + 1]]
    heapq.heapify(heap)
    
    res = []
    i = k + 1
    while heap and i < len(arr):
        min_val = heapq.heappop(heap)
        res.append(min_val)
        heapq.heappush(heap, arr[i])
        i += 1
    
    while heap:
        min_val = heapq.heappop(heap)
        res.append(min_val)
        
    return res
    
arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
print (sort_k_messed_array(arr, k))
    
        
        

