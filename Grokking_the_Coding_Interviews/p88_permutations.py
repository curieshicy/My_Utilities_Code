def find_permutations(nums):
    def dfs(arr, path, res):
        if len(path) == len(nums):
            res.append(path)
            
        for i in range(len(arr)):
            dfs(arr[:i] + arr[i+1:], path + [arr[i]], res)
            
        return res
    return dfs(nums, [], [])

def main():    

    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))

main()
