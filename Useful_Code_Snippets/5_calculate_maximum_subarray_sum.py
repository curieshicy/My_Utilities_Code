# given an array, find its subarray which gives the maximum sum
# e.g. [34, -50, 42, 14, -5, 86] ---> [42, 14, -5, 86] --->137
# e.g. [-5, -1, -8, -9]  ---> 0
# do this in linear time O(n)

def calculate_maximum_subarray_sum(nums):
    # edge case
    if all(num <0 for num in nums):
        return 0
    
    max_sum = 0
    for num in nums:
        if max_sum + num > 0:
            max_sum += num
        else:
            max_sum = 0
    return max_sum

# test
test_1 = [34, -50, 42, 14, -5, 86]
test_2 = [-5, -1, -8, -9]
test_3 = [8, -1, 3, 4]

print (calculate_maximum_subarray_sum(test_1))
print (calculate_maximum_subarray_sum(test_2))
print (calculate_maximum_subarray_sum(test_3))

# follow-up what if the array wraps around
# e.g. [8, -1, 3, 4]  ---> 15
def calculate_minimum_subarray_sum(nums):
    
    if all(num < 0 for num in nums):
        return 0
    
    min_sum = 0
    for num in nums:
        if min_sum + num > min_sum:
            continue
        else:
            min_sum += num
    return min_sum

print (calculate_minimum_subarray_sum(test_1))
print (calculate_minimum_subarray_sum(test_2))
print (calculate_minimum_subarray_sum(test_3))

def calculate_wrap_around_maximum(nums):
    min_sum = calculate_minimum_subarray_sum(nums)
    max_sum = calculate_maximum_subarray_sum(nums)
    wrap_around_maximum = max_sum - min_sum
    return max(wrap_around_maximum, max_sum)


print (calculate_wrap_around_maximum(test_1))
print (calculate_wrap_around_maximum(test_2))
print (calculate_wrap_around_maximum(test_3))


