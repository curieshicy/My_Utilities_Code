import heapq
import bisect
def find_closest_elements(arr, K, X):
    idx_of_x = bisect.bisect_right(arr, X)
    if idx_of_x == len(arr):
        return arr[-K:]
        
    max_heap = []
    for i in range(max(0, idx_of_x - K), min(idx_of_x + K + 1, len(arr))):
        heapq.heappush(max_heap, (-abs(arr[i] - X), arr[i]))
        
    while len(max_heap) > K:
        heapq.heappop(max_heap)
        
    res = []
    while max_heap:
        _, num = heapq.heappop(max_heap)
        res.append(num)
        
    return res
    
def find_closest_elements(arr, K, X):
    idx_of_x = bisect.bisect_right(arr, X)
    if idx_of_x == len(arr):
        return arr[-K:]
        
    min_heap = []
    for i in range(max(0, idx_of_x - K), min(idx_of_x + K + 1, len(arr))):
        heapq.heappush(min_heap, (abs(arr[i] - X), arr[i]))
    
    res = []
    for _ in range(K):
        _, num = heapq.heappop(min_heap)
        res.append(num)
        
    return res

def main():
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))
main()
