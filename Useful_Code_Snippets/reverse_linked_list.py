import unittest
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseLinkedList(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()

        self.head = self.cur = ListNode(1)
        for i in [2, 3, 4, 5]:
            self.cur.next = ListNode(i)
            self.cur = self.cur.next

        self.expected = [5,4,3,2,1]
        
    def testReverseLinkedList(self):
        headnode = self.solution.reverseLinkedList(self.head)
        reversedList = []
        while headnode:
            reversedList.append(headnode.val)
            headnode = headnode.next

        self.assertEqual(reversedList, self.expected)

if __name__ == '__main__':
    unittest.main()
        
        

    
