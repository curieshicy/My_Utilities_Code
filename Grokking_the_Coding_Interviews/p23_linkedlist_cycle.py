class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
def has_cycle(head):
    tortoise = head
    hare = head
    while hare and hare.next    :
        hare = hare.next.next
        tortoise = tortoise.next
        if hare == tortoise:
            return True
    return False

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

main()
