# implement groubpy by scratch
# example: given a string 'aabbbbccca' return [('a', 2), ('b', 4), ('c', 3), ('a', 1)]
from collections import deque
import unittest
from itertools import groupby

class Solution:
    def implement_groupby(self, s):
        pair = []
        m = deque(s)
        char = s[0]
        count = 0
        while m:
            popped = m.popleft()
            if char == popped:
                count += 1
            else:
                pair.append((char, count))
                char = popped
                count = 1       
        pair.append((char, count))
        return pair

    def use_built_in_groupby(self, s):
        pair = []
        for key, group in groupby(s):
            pair.append((key, len(list(group))))
        return pair

class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()
        self.s1 = 'aabbbbcccaa'
        self.s2 = 'abc'

    def expectEqual(self, first, second):
        with self.subTest():
            self.assertEqual(first, second)

    def testImplementGroupby(self):
        self.expectEqual(self.solution.implement_groupby(self.s1), [('a', 2), ('b', 4), ('c', 3), ('a', 2)])
        self.expectEqual(self.solution.implement_groupby(self.s2), [('a', 1), ('b', 1), ('c', 1)])

    def testBuildInGroupby(self):
        self.expectEqual(self.solution.use_built_in_groupby(self.s1), [('a', 2), ('b', 4), ('c', 3), ('a', 2)])
        self.expectEqual(self.solution.use_built_in_groupby(self.s2), [('a', 1), ('b', 1), ('c', 1)])
        
if __name__ == '__main__':
    unittest.main()   
