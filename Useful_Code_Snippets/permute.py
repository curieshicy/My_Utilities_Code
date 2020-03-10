def permute(nums):
    visited = [0] * len(nums)
    res = []

    def dfs(path):
        if len(path) == len(nums):
            res.append(path)

        else:
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = 1
                    dfs(path + [nums[i]])
                    visited[i] = 0

    dfs([])
    return res

print (permute([1,2,3]))
