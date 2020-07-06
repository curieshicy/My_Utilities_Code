# leetcode 238

class productExceptSelf(self, nums):
    output = [1] * len(nums)
    
    prod = 1
    for i in range(len(nums)):
        output[i] *= prod
        prod *= nums[i]
        
    prod = 1
    for i in range(len(nums) -1, -1, -1):
        output[i]*= prod
        prod *= nums[i]
        
    return output
