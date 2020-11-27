def find_pairs_with_specific_difference(nums, k):
    # O(n**2) time
    n = len(nums)
    d = {}
    for idx, val in enumerate(nums):
        d[val] = idx
    res = []
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] - nums[j] == k:
                res.append([nums[i], nums[j]])
            elif nums[j] - nums[i] == k:
                res.append([nums[j], nums[i]])
    res_w_idx = [(x, y, d[y]) for x, y in res]
    res_w_idx.sort(key = lambda t: t[2])
    return [[x,y] for x, y, idx in res_w_idx]

def find_pairs_with_specific_difference_1(nums, k):
    # O(nlogn) time
    def binary_search(arr, start, end, key):
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                start += 1
            else:
                end -= 1
        return -1
	
    d = {}
    for idx, val in enumerate(nums):
        d[val] = idx
    nums.sort()
    res = []
    for i, num in enumerate(nums):
        idx = binary_search(nums, i + 1, len(nums) - 1, num + k)
        if idx == -1:
            continue
        res.append([nums[idx], num])
    res_w_idx = [(x, y, d[y]) for x, y in res]
    res_w_idx.sort(key = lambda t: t[2])
    return [[x,y] for x, y, idx in res_w_idx]
    
def find_pairs_with_specific_difference_2(nums, k):
    # O(n) time; O(n) space
    d = {} # num : idx
    res = []
    for idx, num in enumerate(nums):
        if num + k in d:
            res.append([num + k, num])
        if num - k in d:
            res.append([num, num - k])
        d[num] = idx

    buckets = [None for i in range(len(nums))]
    for x, y in res:
        buckets[d[y]] = [x,y]

    ans = []
    for bucket in buckets:
        if bucket != None:
            ans.append(bucket)
    return ans
    
nums1 = [0, -1, -2, 2, 1]
nums2 = [0, -1, -2, 2, 1]
nums3 = [0, -1, -2, 2, 1]
k = 1
print (find_pairs_with_specific_difference(nums1, k))
print (find_pairs_with_specific_difference_1(nums2, k))
print (find_pairs_with_specific_difference_2(nums3, k))
