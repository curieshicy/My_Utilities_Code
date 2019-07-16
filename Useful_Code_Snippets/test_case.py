import unittest

class Solution:
    def find_max_val(self, nums):
        max_val = float('-inf')
        for num in nums:
            max_val = max(max_val, num)
        return max_val


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()
        self.nums = [1,2,3,4,5,6,7]

    def test_find_max_val(self):
        self.assertEqual(self.solution.find_max_val(self.nums), 7)

if __name__ == '__main__':
    unittest.main()
