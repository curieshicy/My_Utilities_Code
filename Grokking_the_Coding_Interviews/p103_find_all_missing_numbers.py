def find_missing_numbers(nums):
    missingNumbers = []
    n = len(nums)
    all_numbers = [i for i in range(1, n + 1)]
    nums_set = set(nums)
    for num in all_numbers:
        if num not in nums_set:
            missingNumbers.append(num)
    return missingNumbers

def find_missing_numbers(nums):
    missingNumbers = []
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    print (nums)
    for i in range(n):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)
            
    return missingNumbers

def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


main()
