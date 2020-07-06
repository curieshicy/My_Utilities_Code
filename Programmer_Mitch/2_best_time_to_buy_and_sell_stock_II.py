# leetcode #122
class Solution:
    def maxProfit(self, prices):
        total = 0
        
        for i in range(1, len(prices)):
            total += max(prices[i] - prices[i-1], 0)
        
        return total
