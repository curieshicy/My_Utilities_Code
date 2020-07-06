# leetcode # 189
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        
    
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -=1
