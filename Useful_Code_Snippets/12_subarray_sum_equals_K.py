def subarraySum(nums, k):
    
    d = {0:1}
    
    _sum, count = 0, 0
    for num in nums:
        _sum += num
        count += d.get(_sum - k, 0)
        d[_sum] = d.get(_sum, 0) + 1
    
        print (_sum, count, d)

    return count

# test
print (subarraySum([1, -1, 2, 3], 2))
#print (subarraySum([28,54,7,-70,22,65,-6], 100))
