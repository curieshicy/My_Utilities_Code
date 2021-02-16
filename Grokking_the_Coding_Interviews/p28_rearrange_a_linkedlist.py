from __future__ import print_function

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
        print(str(temp.value) + " ", end='')
        temp = temp.next
    print()

def reorder(head):
    # find the middle
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    def reverse_list(node):
        prev = None
        cur = node
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
        
    second_half = reverse_list(slow)
    first_half = head
    dummy = Node(0)
    new_head = dummy
           
    while first_half and second_half:
        new_head.next = first_half
        first_half = first_half.next
        new_head = new_head.next
        
        new_head.next = second_half
        second_half = second_half.next
        new_head = new_head.next
        
    return dummy.next


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    #head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()
