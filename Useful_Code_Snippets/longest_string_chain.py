import unittest
class Solution:
    def longestStringChain(self, words):
        dp = {}
        for word in words:
            dp[word] = max(dp.get(word[:i] + word[i+1:], 0) + 1 for i in range(len(word)))

        return max(dp.values())
        

class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.strings = ['a', 'b', 'ba', 'bca', 'bda', 'bdca']
        self.solution = Solution()

    def testLongestStringChain(self):
        self.assertEqual(self.solution.longestStringChain(self.strings), 4)

if __name__ == '__main__':
    unittest.main()
