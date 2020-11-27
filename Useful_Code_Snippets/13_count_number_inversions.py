## http://mijkenator.github.io/2016/12/10/2016-12-10-mergesort-inversion-count/ ##

import unittest
class Solution:

    def mergeSort(self, nums):
        if len(nums) < 2:
            return nums, 0

        mid_idx = len(nums) // 2

        left, a = self.mergeSort(nums[:mid_idx])
        right, b = self.mergeSort(nums[mid_idx:])
        res, c =  self.mergeSortHelper(left, right)
        print (a, b, c)
        return res, a + b + c

    def mergeSortHelper(self, nums1, nums2):
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        res = []
        count = 0
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                count += m - i
                res.append(nums2[j])
                j += 1

        while i < m:
            res.append(nums1[i])
            i += 1

        while j < n:
            res.append(nums2[j])
            j += 1

        return res, count


class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()
        self.arr = [6,2,1,3]

    def testQuickSort(self):
        self.assertEqual(self.solution.mergeSort(self.arr)[1], 4)

if __name__ == '__main__':
    unittest.main()
