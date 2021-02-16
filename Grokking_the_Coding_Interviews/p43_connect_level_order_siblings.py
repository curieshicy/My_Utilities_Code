from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    if not root:
        return 
    queue = deque([root])
    while queue:
        nodes_at_each_level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            nodes_at_each_level.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        if len(nodes_at_each_level) == 1:
            nodes_at_each_level[0].next = None
            
        cur_node = nodes_at_each_level[0]
        for i in range(1, len(nodes_at_each_level)):
            cur_node.next = nodes_at_each_level[i]
            cur_node = cur_node.next
        cur_node.next = None
    return
    
    
def connect_level_order_siblings_1(root):
    if not root:
        return 
    queue = deque([root])
    while queue:
        prev_node = None
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            if prev_node:
                prev_node.next = cur_node
            
            prev_node = cur_node
            
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
                
    return

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings_1(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()

