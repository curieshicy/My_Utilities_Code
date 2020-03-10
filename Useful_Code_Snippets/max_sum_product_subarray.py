def max_product_subarray(arr):
    best = 0
    local = arr[0]
    for i in range(1, len(arr)):
        local = max(arr[i], local * arr[i])
        best = max(best, local)

    return best

def max_sum_subarray(arr):
    best = 0
    local = arr[0]
    for i in range(1, len(arr)):
        local = max(arr[i], local + arr[i])
        best = max(best, local)

    return best

nums = [2,250,1, -10, -1, -100, 0]
print (max_product_subarray(nums))
print (max_sum_subarray(nums))
