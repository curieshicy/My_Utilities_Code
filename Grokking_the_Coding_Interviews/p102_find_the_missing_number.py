def find_missing_number(nums):
    n = len(nums)
    expected_sum = (n + 1) * n // 2 
    cur_sum = sum(nums)
    return expected_sum - cur_sum
    
def find_missing_number(nums):
    # sort nums
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i]
        if j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i
    
    return n

def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([0, 1, 2, 3]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
main()
