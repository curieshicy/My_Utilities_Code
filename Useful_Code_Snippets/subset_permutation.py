import unittest
class Solution:

    def permute(self, nums):
        res = []
        self.dfsPermute(nums, [], res)
        return res

    def dfsPermute(self, arr, path, res):
        if not arr:
            res.append(path)

        for i in range(len(arr)):
            self.dfsPermute(arr[:i] + arr[i+1:], path + [arr[i]], res)
        
    def subset(self, nums):
        res = []
        self.dfsSubset(nums, 0, [], res)
        return res

    def dfsSubset(self, arr, index, path,res):
        res.append(path)
        for i in range(index, len(arr)):
            self.dfsSubset(arr, i+1, path + [arr[i]], res)

solution = Solution()
print (solution.permute([1,2,3]))
print (solution.subset([1,2,3]))




    
