import random
import unittest

class Solution:
    def selection_sort(self, nums):
        def find_min_idx(arr):
            idx, val = 0, arr[0]
            for i in range(1, len(arr)):
                if arr[i] < val:
                    idx, val = i, arr[i]
            return idx

        sorted_nums = []

        for i in range(len(nums)):
            idx  = find_min_idx(nums)
            sorted_nums.append(nums.pop(idx))

        return sorted_nums


    def quick_sort(self, nums):
        # base case
        if len(nums) < 2:
            return nums

        idx = 0
        pivot = nums[idx]
        less_than_pivot = [nums[i] for i in range(idx + 1, len(nums)) if nums[i] <= pivot]
        greater_than_pivot = [nums[i] for i in range(idx + 1, len(nums)) if nums[i] > pivot]

        return self.quick_sort(less_than_pivot) + [pivot] + self.quick_sort(greater_than_pivot)


    def merge_sort(self, num1, num2): # for merge_sort, num1 and num2 need to be sorted first.
        res = []
        i = j = 0
        while i < len(num1) and j <len(num2):
            if num1[i] <= num2[j]:
                res.append(num1[i])
                i += 1
            else:
                res.append(num2[j])
                j +=1

        while i < len(num1):
            res.append(num1[i])
            i += 1

        while j < len(num2):
            res.append(num2[j])
            j += 1

        return res

    def bubble_sort(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                
        return nums

class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()
        self.nums = [156, 141, 35, 94, 88, 61, 111]
        self.num1 = [156, 141, 35]
        self.num2 = [94, 88, 61, 111]
        self.num1.sort()
        self.num2.sort()

    def test_selection_sort(self):
        self.assertEqual(self.solution.selection_sort(self.nums), [35, 61, 88, 94, 111, 141, 156])

    def test_quick_sort(self):
        self.assertEqual(self.solution.quick_sort(self.nums), [35, 61, 88, 94, 111, 141, 156])

    def test_merge_sort(self):
        self.assertEqual(self.solution.merge_sort(self.num1, self.num2), [35, 61, 88, 94, 111, 141, 156])

    def test_bubble_sort(self):
        self.assertEqual(self.solution.bubble_sort(self.nums), [35, 61, 88, 94, 111, 141, 156])

if __name__ == '__main__':
    unittest.main()     
