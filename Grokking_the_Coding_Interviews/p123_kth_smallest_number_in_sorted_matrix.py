import heapq
def find_Kth_smallest(matrix, k):
    min_heap = []
    for row in matrix:
        heapq.heappush(min_heap, (row[0], 0, row))
    
    kth_smallest = None
    while k:
        number, idx, arr = heapq.heappop(min_heap)
        kth_smallest = number
        
        if idx < len(arr) - 1:
            heapq.heappush(min_heap, (arr[idx + 1], idx + 1, arr))
            
        k -= 1
        
    return kth_smallest
        


def main():
    print("Kth smallest number is: " + str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

main()
