from heapq import *
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_lists(lists):
    min_heap = []
    count = 0
    for head in lists:
        if head:
            count += 1
            heappush(min_heap, (head.value, count, head))
            
    
    res_head, tail_node = None, None
    while min_heap:
        _, _, node = heappop(min_heap)
        if not res_head:
            res_head = node
            tail_node = node
            
        else:
            tail_node.next = node
            tail_node = tail_node.next
            
        if node.next:
            count += 1
            heappush(min_heap, (node.next.value, count, node.next))
    
    return res_head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next

main()
