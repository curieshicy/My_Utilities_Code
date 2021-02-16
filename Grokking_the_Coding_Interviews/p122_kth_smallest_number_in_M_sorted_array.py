import heapq
def find_Kth_smallest(lists, k):
    total_num = 0
    for arr in lists:
        total_num += len(arr)
        
    if total_num < k:
        return None
        
    number = None
    min_heap = []
    for arr in lists:
        heapq.heappush(min_heap, (arr[0], 0, arr))
        
    while k:
        num, idx, arr = heapq.heappop(min_heap)
        number = num
        
        if idx < len(arr) - 1:
            heapq.heappush(min_heap, (arr[idx + 1], idx + 1, arr))
                
        k -= 1

    return number


def main():
    print("Kth smallest number is: " + str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    print("Kth smallest number is: " + str(find_Kth_smallest([[5, 8, 9], [1, 7]], 3)))


main()
