
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

def combination(nums, k):
    res = []
    def dfs(arr, path):        
        if len(path) == k:
            res.append(path)
            
        for i in range(len(arr)):
            dfs(arr[i+1:], path + [arr[i]])    
    dfs(nums, [])
    return res

def letterCombinations(digits):    
    kvmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', 
              '8': 'tuv', '9': 'wxyz'}
    
    res = []
    def dfs(nums, start_idx, path):
        if len(path) == len(nums):
            res.append(path)
            return
        
        for char in kvmaps[nums[start_idx]]:
            dfs(nums, start_idx + 1, path + char)
            
    dfs(digits, 0, '')
    return res

print (permutation([1,2,3]))
print (subset([1,2,3]))
print (combination([1,2,3,4], 2))
