def triplet_with_smaller_sum(arr, target):
    count = 0
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        target_sum = target - arr[i]
        l = i + 1
        h = n - 1
        while l < h:
            if arr[l] + arr[h] >= target_sum:
                h -= 1
            else:
                count += (h - l)
                l += 1
    
    return count
    
def triplet_with_smaller_sum_follow_up(arr, target):
    # return all such triplets
    triplets = []
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        target_sum = target - arr[i]
        l = i + 1
        h = n - 1
        while l < h:
            if arr[l] + arr[h] >= target_sum:
                h -= 1
            else:
                for k in range(l + 1, h + 1):
                    triplets.append([arr[i], arr[l], arr[k]])
                l += 1
    return triplets

        
test_1 = [-1,0,2,3]
test_2 = [-1, 4, 2, 1, 3]
print (triplet_with_smaller_sum(test_1, 3))
print (triplet_with_smaller_sum(test_2, 5))
print (triplet_with_smaller_sum_follow_up(test_1, 3))
print (triplet_with_smaller_sum_follow_up(test_2, 5))
