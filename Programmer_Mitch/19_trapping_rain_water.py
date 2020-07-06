# leetcode 42

class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_wall, right_wall = 0, 0
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_wall:
                    left_wall = height[left]
                else:
                    water += left_wall - height[left]
                left += 1
            else:
                if height[right] >= right_wall:
                    right_wall = height[right]
                else:
                    water += right_wall - height[right]
                right -=1
        return water
                    
