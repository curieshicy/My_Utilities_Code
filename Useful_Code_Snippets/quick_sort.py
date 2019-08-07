import unittest
import random

class Solution:

    def quickSort(self, nums):
        if len(nums) < 2:
            return nums

        pivot = random.choice(nums)
        left, mid, right = [], [], []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                mid.append(num)

        return self.quickSort(left) + mid + self.quickSort(right)


class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()
        self.arr = [5, 1, 1, 2, 0, 0]

    def testQuickSort(self):
        self.assertEqual(self.solution.quickSort(self.arr), [0,0,1,1,2,5])

if __name__ == '__main__':
    unittest.main()
        
