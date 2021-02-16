def search_quadruplets(arr, target):
    arr.sort()
    quadruples = []
    for i in range(len(arr) - 3):
        for j in range(i + 1, len(arr) -2):
            target_sum = target - arr[i] - arr[j]
            l = j + 1
            h = len(arr) - 1
            while l < h:
                two_sum = arr[l] + arr[h]
                if two_sum == target_sum:
                    quadruples.append([arr[i], arr[j], arr[l], arr[h]])
                    l += 1
                    h -= 1
                    
                elif two_sum < target_sum:
                    l += 1
                else:
                    h -= 1
    return quadruples
    

test_1 = [4, 1, 2, -1, 1, -3]
test_2 = [2, 0, -1, 1, -2, 2]

print (search_quadruplets(test_1, 1))
print (search_quadruplets(test_2, 2))
    
