class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
def find_cycle_length(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            new_slow = slow
            break
            
    cycle_length = 1
    new_slow = new_slow.next
    while new_slow != slow:
        new_slow = new_slow.next
        cycle_length += 1
        
    return cycle_length
            

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
