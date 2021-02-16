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

def reverse_list(head):
    prev, cur, _next = None, head, None
    while cur:
        _next = cur.next
        cur.next = prev
        prev = cur
        cur = _next
    return prev

def reverse_sub_list(head, p, q):
    cur_head = head
    while cur_head.next.value != p:
        cur_head = cur_head.next
    
    tail_node_section_1 = cur_head
    head_node_section_2 = cur_head.next
    # cut the connection between section 1 and 2
    cur_head.next = None

    cur = head_node_section_2
    while cur.value != q:
        cur = cur.next
        
    head_node_section_3 = cur.next
    # cut the connection between section 2 and 3
    cur.next = None
    
    new_head_node_section_2 = reverse_list(head_node_section_2)
    
    # connects 1 and 2
    tail_node_section_1.next = new_head_node_section_2
    # connects 2 and 3
    new_cur =  new_head_node_section_2
    while new_cur.next:
        new_cur = new_cur.next
    new_cur.next = head_node_section_3
    
    return head
    

def reverse_sub_list(head, p, q):
    if p == q:
        return head
        
    prev, cur = None, head
    
    for i in range(p - 1):
        prev = cur 
        cur = cur.next
        
    last_node_of_first_section = prev
    last_node_of_second_section = cur
    
    for i in range(q - p + 1):
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        
    if last_node_of_first_section:
        last_node_of_first_section.next = prev
    else:
        # p = 1
        head = prev
        
    last_node_of_second_section.next = cur
    
    return head
    

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
main()
