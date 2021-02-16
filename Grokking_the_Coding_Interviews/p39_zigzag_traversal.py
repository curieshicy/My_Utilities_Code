from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []
    level_num = 1
    queue = deque([root])
    while queue:
        nodes_at_level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            nodes_at_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if level_num % 2 == 1:
            result.append(nodes_at_level)
        else:
            result.append(nodes_at_level[::-1])
        level_num += 1
    return result

def traverse_use_deque(root):
    result = []
    left_to_right = True
    queue = deque([root])
    while queue:
        nodes_at_level = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if left_to_right:
                nodes_at_level.append(node.val)
            else:
                nodes_at_level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(nodes_at_level))
        left_to_right = not left_to_right
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse_use_deque(root)))


main()
