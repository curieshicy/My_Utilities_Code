
def maxMoney(nums):

    res = [0]*len(nums)
    res[0] = nums[0]
    res[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        res[i] = max(res[i-1], nums[i] + res[i-2])

    return res


def maxMoney_modify(nums):

    res = [0]*len(nums)
    res[0] = nums[0]
    res[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        res[i] = max(res[i-1], nums[i] + res[i-2])

    return res


# test
m1 = [2, 3, 5, 7, 4, 8, 100] # 109
m2 = [100, 3, 5, 7, 4, 8, 2] # 109
print (maxMoney_modify(m1))
print (maxMoney_modify(m2))

    
