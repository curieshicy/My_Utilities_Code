def permute(num):
    if len(num) == 0: return []
    if len(num) == 1: return [num]
    res = []
    for i in range(len(num)):
        for j in permute(num[:i] + num[i+1:]):
            res.append([num[i]] + j)
    return res

print (permute([1,2,3]))
