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


def reverse_alternate_k_elements(head, k):
    if not head or k <= 1:
        return head
        
    prev, cur = None, head
    while True:
        last_node_prev_section = prev
        last_node_sub_list = cur
        
        i = 0
        while cur and i < k:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            i += 1
            
        if last_node_prev_section:
            last_node_prev_section.next = prev
        else:
            head = prev
            
        last_node_sub_list.next = cur
        prev = last_node_sub_list
        
        j = 0
        while cur and j < k:
            prev = cur
            cur = cur.next
            j += 1
        
        if not cur:
            break
    
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
main()
