
def permutation(nums):
    res = []
    def dfs(arr, path):
        if not arr:
            res.append(path)

        for i in range(len(arr)):
            dfs(arr[:i] + arr[i+1:], path + [arr[i]])
    dfs(nums, [])
    return res


def subset(nums):
    res = []
    def dfs(arr, index, path):
        res.append(path)
        for i in range(index, len(arr)):
            dfs(arr, i + 1, path + [arr[i]])
    dfs(nums, 0, [])
    return res

print (permutation([1,2,3]))
print (subset([1,2,3]))
