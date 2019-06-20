import unittest
class Solution:
    def longestTurbulentArray(self, num):
        best, local = 0, 0
        for i in range(len(num)):
            if i >=2 and (num[i-2]<num[i-1]>num[i] or num[i-2]>num[i-1]<num[i]):
                local += 1
            elif i>=1 and num[i] != num[i-1]:
                local = 2
            else:
                local = 1
            best = max(best, local)
        return best
            
    def longestNonrepeatString(self, s):
        start = 0; length = 0; seenChar = dict()
        for i in range(len(s)):
            if s[i] in seenChar:
                start = max(start, seenChar[s[i]] + 1)
                
            length = max(length, i - start + 1)
            seenChar[s[i]] = i
        return length
            
            

    def longestMaximumSubarray(self, arr):
        # [-1, 2, 3, 4, -5]
        best = local = arr[0]
        for i in range(1, len(arr)):
            local = max(arr[i], local + arr[i])
            best = max(local, best)

        return best

class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()
        self.num = [1,2,3,4,5]
        self.string = 'abcabcab'
        self.array = [-1, 2, 3, 4, -5]

    def testLongestTurbulentArray(self):
        self.assertEqual(self.solution.longestTurbulentArray(self.num), 2)

    def testLongestNonrepeatString(self):
        self.assertEqual(self.solution.longestNonrepeatString(self.string), 3)

    def testLongestMaximumSubarray(self):
        self.assertEqual(self.solution.longestMaximumSubarray(self.array), 9)

if __name__ == '__main__':
    unittest.main()   
        
        
