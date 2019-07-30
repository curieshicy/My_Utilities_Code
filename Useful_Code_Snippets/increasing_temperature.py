import unittest
class Solution:

    def increaseTemp(self, T):
        res = [0 for i in range(len(T))]
        stack = []

        for i, temp in enumerate(T):
            while stack and stack[-1][1] < temp:
                prev_i = stack.pop()[0]
                res[prev_i] = i - prev_i
            stack.append([i, temp])

        return res

class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()
        self.temp = [73, 74, 75, 71, 69, 72, 76, 73]
        self.ans = [1, 1, 4, 2, 1, 1, 0, 0]

    def testIncreaseTemp(self):
        self.assertEqual(self.solution.increaseTemp(self.temp), self.ans)

if __name__ == '__main__':
    unittest.main()
