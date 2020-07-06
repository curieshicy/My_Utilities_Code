# leetcode 628
class Solution:
    def maximumProduct(self, nums):
        highest_product_of_three = nums[0] * nums[1] * nums[2]
        highest_product_of_two = nums[0] * nums[1]
        lowest_product_of_two = nums[0] * nums[1]
        
        highest_max = max(nums[0], nums[1])
        lowest_min = min(nums[0], nums[1])
        
        for n in nums[2:]:
            highest_product_of_three = max(highest_product_of_three,
                                           n * highest_product_of_two,
                                           n * lowest_product_of_two)
                                           
            highest_product_of_two = max(highest_product_of_two,
                                         n * highest_max,
                                         n * lowest_min)

            lowest_product_of_two = min(lowest_product_of_two, n * highest_max, n * lowest_min)
            
            highest_max = max(highest_max, n)
            lowest_min = min(lowest_min, n)
            
        return highest_product_of_three
        
class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3],
                   nums[-1] * nums[0] * nums[1])


class Solution:
    def maximumProduct(self, nums):
        min1 = min2 = sys.maxint
        max1 = max2 = max3 = -sys.maxint - 1
        
        for n in nums:
            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
                
            elif n >= max2:
                max3 = max2
                max2 = n
            
            elif n >= max3:
                max3 = n
            
            if n<= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n
        
        return max(max1 * max2 * max3, max1 * min1 * min2)
            
