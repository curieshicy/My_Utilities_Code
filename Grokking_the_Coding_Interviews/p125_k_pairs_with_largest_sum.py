import heapq
def find_k_largest_pairs(nums1, nums2, k):
    result = []
    max_heap = []
    
    i = 0
    j = 0
    
    while len(max_heap) < k:
        if i + 1 < len(nums1) and j + 1 < len(nums2):
            heapq.heappush(max_heap, (-nums1[i] - nums2[j], (nums1[i], nums2[j])))
            heapq.heappush(max_heap, (-nums1[i + 1] - nums2[j], (nums1[i + 1], nums2[j])))
            heapq.heappush(max_heap, (-nums1[i] - nums2[j + 1], (nums1[i], nums2[j + 1])))
            heapq.heappush(max_heap, (-nums1[i + 1] - nums2[j + 1], (nums1[i + 1], nums2[j + 1])))
            i += 1
            j += 1
            
    while max_heap and k:
        _, pair = heapq.heappop(max_heap)
        result.append(list(pair))
        k -= 1
    
    return result

def find_k_largest_pairs(nums1, nums2, k):
    min_heap = []
    for i in range(min(len(nums1), k)):
        for j in range(min(len(nums2), k)):
            if len(min_heap) < k:
                heapq.heappush(min_heap, (nums1[i] + nums2[j], (nums1[i], nums2[j])))
            else:
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    heapq.heappushpop(min_heap, (nums1[i] + nums2[j], (nums1[i], nums2[j])))
                
    result = []
    while min_heap:
        _, pair = heapq.heappop(min_heap)
        result.append(list(pair))
        
    return result

def main():
    print("Pairs with largest sum are: " + str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))
    print("Pairs with largest sum are: " + str(find_k_largest_pairs([5, 2, 1], [2, -1], 3)))


main()
