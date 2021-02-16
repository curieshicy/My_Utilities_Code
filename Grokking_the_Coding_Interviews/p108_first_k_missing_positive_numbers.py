def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    extra_nums = set()
    for i in range(n):
        if nums[i] != i + 1 and k != 0:
            missingNumbers.append(i + 1)
            extra_nums.add(nums[i])
            k -= 1
            
    if not missingNumbers:
        for i in range(k):
            missingNumbers.append(n + i + 1)
        return missingNumbers
        
    cur_num = n
    while k:
        cur_num += 1
        if cur_num not in extra_nums:
            missingNumbers.append(cur_num)
            k -= 1
        
    return missingNumbers


def main():
    print (find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print (find_first_k_missing_positive([2, 3, 4], 3))
    print (find_first_k_missing_positive([-2, -3, 4], 2))
main()
