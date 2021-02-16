import heapq
def find_smallest_range(lists):
    range_min = float('-inf')
    range_max = float('inf')
    max_num = float('-inf')
    
    min_heap = []
    n = len(lists)
    for i in range(n):
        heapq.heappush(min_heap, (lists[i][0], 0, lists[i]))
        max_num = max(max_num, lists[i][0])
        
    while len(min_heap) == n:
        num, idx, arr = heapq.heappop(min_heap)
        if max_num - num < range_max - range_min:
            range_max = max_num
            range_min = num
        
        if idx < len(arr) - 1:
            heapq.heappush(min_heap, (arr[idx + 1], idx + 1, arr))
            max_num = max(max_num, arr[idx + 1])

    return [range_min, range_max]


def main():
  print("Smallest range is: " + str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
