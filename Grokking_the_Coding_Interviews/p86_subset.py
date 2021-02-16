def find_subsets(nums):
    def dfs(arr, path, index, res):
        res.append(path)
        for i in range(index, len(arr)):
            dfs(arr, path + [arr[i]], i + 1, res)
        return res
        
    subsets = dfs(nums, [], 0, [])
    return subsets

def find_subsets(nums):
    subsets = []
    subsets.append([])
    for num in nums:
        n = len(subsets)
        for i in range(n):
            subsets.append(subsets[i] + [num])
    return subsets

def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
