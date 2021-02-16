import heapq, collections
def find_k_frequent_numbers(nums, k):
    d = collections.defaultdict(int)
    for num in nums:
        d[num] += 1
    
    freq_num = [(freq, num) for num, freq in d.items()]
    min_heap = []
    for i in range(k):
        heapq.heappush(min_heap, freq_num[i])
        
    for i in range(k, len(d)):
        if freq_num[i][0] > min_heap[0][0]:
            heapq.heappushpop(min_heap, freq_num[i])
            
    res = []
    for _, num in min_heap:
        res.append(num)

    return res


def main():
    print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))
main()
