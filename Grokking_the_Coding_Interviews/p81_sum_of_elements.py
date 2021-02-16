import heapq
def find_sum_of_elements(nums, k1, k2):
    # maintain a max heap of size k2 - 1
    max_heap = []
    for i in range(len(nums)):
        if i < k2 - 1:
            heapq.heappush(max_heap, -nums[i])
        else:
            if nums[i] < -max_heap[0]:
                heapq.heappushpop(max_heap, -nums[i])
                
    summation = 0
    for i in range(k2 - k1 - 1):
        summation += -heapq.heappop(max_heap)
    
    return summation

def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
