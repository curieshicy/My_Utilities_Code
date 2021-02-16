from __future__ import print_function

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate(head, rotations):
    length = 0
    dummy = head
    while dummy:
        dummy = dummy.next
        length += 1
    
    steps = rotations % (length + 1)
    if steps == 0 or rotations == 0:
        return head
    
    cur1 = head
    cur2 = head
    i = 0
    while i < steps:
        cur2 = cur2.next
        i += 1
        
    ans = cur2
    i = 0
    while i < length - steps - 1:
        cur2 = cur2.next
        i += 1
    tail = cur2
    
    tail.next = cur1
    i = 0
    while i < steps - 1:
        cur1 = cur1.next
        i += 1
    cur1.next = None
    
    return ans

def rotate(head, rotations):
    if not head or not head.next or rotations <= 0:
        return head
        
    length = 1
    cur_last_node = head
    while cur_last_node.next:
        cur_last_node = cur_last_node.next
        length += 1
    
    cur_last_node.next = head # make it circular
    rotations %= length
    skip_length = length - rotations
    
    last_node_rotated_list = head
    for i in range(skip_length - 1):
        last_node_rotated_list = last_node_rotated_list.next
    
    head = last_node_rotated_list.next
    last_node_rotated_list.next = None
    return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()
    
    
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 8)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()
main()
