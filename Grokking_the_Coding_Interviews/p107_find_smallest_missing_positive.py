def find_first_smallest_missing_positive(nums):
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    print (nums)
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
            
    return len(nums) + 1

def main():
    print (find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
    print (find_first_smallest_missing_positive([-3, -2, 0, 1, 2]))
    print (find_first_smallest_missing_positive([3, 2, 5, 1]))
    print (find_first_smallest_missing_positive([10, 5, 100]))
    print (find_first_smallest_missing_positive([1,2,3]))
main()
