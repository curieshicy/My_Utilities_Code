import heapq
from collections import defaultdict
def find_maximum_distinct_elements(nums, k):
    inf = float('inf')
    d = defaultdict(int)
    for num in nums:
        d[num] += 1
    
    min_heap = []
    for num, freq in d.items():
        if freq == 1:
            heapq.heappush(min_heap, inf)
        else:
            heapq.heappush(min_heap, freq)
            
    distinct_count = 0
    while k:
        if min_heap[0] == inf:
            heapq.heappop(min_heap)
        else:
            pop_num = heapq.heappop(min_heap)
            pop_num -= 1
            if pop_num == 1:
                heapq.heappush(min_heap, inf)
            else:
                heapq.heappush(min_heap, pop_num)
        k -= 1
    
    for num in min_heap:
        if num == inf:
            distinct_count += 1
            
    return distinct_count
    
def main():
    print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))
main()
