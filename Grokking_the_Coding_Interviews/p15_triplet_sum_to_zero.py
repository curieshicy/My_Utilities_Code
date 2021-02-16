def search_triplets(arr):
    if len(arr) < 3:
        return []
    arr.sort()
    ans = []
    n = len(arr)
    for i in range(n - 2):
        expected_num = -arr[i]
        left = i + 1
        right = n - 1
        while left < right:
            local_sum = arr[left] + arr[right]
            if local_sum == expected_num:
                ans.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif local_sum < expected_num:
                left += 1
            else:
                right -= 1
                
                
    return ans
test_1 = [-3, 0, 1, 2, -1, 1, -2]
test_2 = [-5, 2, -1, -2, 3]
print (search_triplets(test_1))
print (search_triplets(test_2))
    
