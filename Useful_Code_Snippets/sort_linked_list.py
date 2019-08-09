import unittest
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def sortLinkedList(self, head):
        if not head or not head.next:
            return head

        middle = self.findMiddleNode(head)
        right = middle.next
        middle.next = None

        return self.mergeTwoSortedLists(self.sortLinkedList(head), self.sortLinkedList(right))
        
    def findMiddleNode(self, head):
        
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def mergeTwoSortedLists(self, l1, l2):
        if not l1:
            return l2

        if not l2:
            return l1

        cur = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next

            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next

        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        return dummy.next


class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()
        self.cur1 = self.h1 = ListNode(1)
        for i in [5, 4, 2, 3]:
            self.cur1.next = ListNode(i)
            self.cur1 = self.cur1.next

        self.expected = [1,2,3,4,5]

    def testSortLinkedList(self):
        sortedList = []
        head = self.solution.sortLinkedList(self.h1)
        while head:
            sortedList.append(head.val)
            head = head.next
        self.assertEqual(sortedList, self.expected)

if __name__ == '__main__':
    unittest.main()
