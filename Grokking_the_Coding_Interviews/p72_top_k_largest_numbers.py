import heapq
def find_k_largest_numbers(nums, k):
    heapq.heapify(nums)
    return heapq.nlargest(k, nums)

def find_k_largest_numbers(nums, k):
    result = []
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)
        
    for _ in range(k):
        max_num = heapq.heappop(max_heap)
        result.append(-max_num)
        
    return result
    
def find_k_largest_numbers(nums, k):
    # construct a min_heap with k numbers
    min_heap = []
    for i in range(k):
        heapq.heappush(min_heap, nums[i])
        
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heapq.heappushpop(min_heap, nums[i])
            
    return min_heap
    

def main():

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))
    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
