def dutch_flag_sort(arr):
    n = len(arr)
    i = 0
    j = 0
    k = n - 1
    while j <= k:
        if arr[j] == 1:
            j += 1
        elif arr[j] == 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
            i += 1
        else:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
            
    return arr

test_1 = [1, 0, 2, 1, 0]
test_2 = [2, 2, 0, 1, 2, 0]
print (dutch_flag_sort(test_1))
print (dutch_flag_sort(test_2))
