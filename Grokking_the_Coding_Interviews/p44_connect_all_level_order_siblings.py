from __future__ import print_function
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    if not root:
        return root
    
    dummy_node = TreeNode(0)
    cur_node = dummy_node
    queue = deque([root])
    while queue:
        node = queue.popleft()
        cur_node.next = node
        cur_node = cur_node.next
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return dummy_node.next


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()
    
main()
