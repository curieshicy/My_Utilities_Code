class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    if not head or not head.next:
        return True
    # find the middle of the linked list
    fast = slow = head
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
    
    new_middle = reverse_list(slow)
    
    # compare first half and second half
    cur = head  
    while cur and new_middle:
        if cur.value != new_middle.value:
            return False
        cur = cur.next
        new_middle = new_middle.next
        
    return True      
    
def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    #head.next.next.next.next.next = Node(2)
    #print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
