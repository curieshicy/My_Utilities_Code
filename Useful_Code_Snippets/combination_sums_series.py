class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(nums, index, target, path):
            if target < 0:
                return
            
            if target == 0:
                res.append(path)
            
            for i in range(index, len(nums)):
                dfs(nums, i, target - nums[i], path + [nums[i]])
        
        candidates.sort()
        dfs(candidates, 0, target, [])
        return res

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(nums, index, target, path):
            if target < 0:
                return
            
            if target == 0:
                res.append(path)
                
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                dfs(nums, i + 1, target - nums[i], path + [nums[i]])
                
        candidates.sort()
        dfs(candidates, 0, target, [])
        return res


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        res = []
        def dfs(nums, index, target, k, path):
            if target == 0 and k == 0:
                res.append(path)
            
            if target < 0 or k < 0:
                return
            
            for i in range(index, len(nums)):
                dfs(nums, i + 1, target - nums[i], k - 1, path + [nums[i]])
                
        dfs(candidates, 0, n, k, [])
        return res

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        if not nums or min(nums) > target:
            return 0
        
        dp = [0 for i in range(target + 1)]
        for num in nums:
            if num <= target:
                dp[num] = 1

        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        
        return dp[-1]
       
        
