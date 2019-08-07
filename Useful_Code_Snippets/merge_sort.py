import unittest
class Solution:

    def mergeSort(self, nums):
        if len(nums) < 2:
            return nums

        mid_idx = len(nums) // 2

        left, right = self.mergeSort(nums[:mid_idx]), self.mergeSort(nums[mid_idx:])
        return self.mergeSortHelper(left, right)

    def mergeSortHelper(self, nums1, nums2):
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        res = []
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < m:
            res.append(nums1[i])
            i += 1

        while j < n:
            res.append(nums2[j])
            j += 1

        return res


class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()
        self.arr = [5, 1, 1, 2, 0, 0]

    def testQuickSort(self):
        self.assertEqual(self.solution.mergeSort(self.arr), [0,0,1,1,2,5])

if __name__ == '__main__':
    unittest.main()                                      
