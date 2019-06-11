# this is to implement level order traversal of a binary tree using both iterative and recursive methods
from collections import deque
import sys
import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:

    def levelOrderTraversalIterative(self, root):

        if not root:
            return []

        queue = deque([root])
        res = []
        depth = 0

        while queue:
            res.append([])
            for i in range(len(queue)):
                node = queue.popleft()
                res[depth].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return res

    def levelOrderTraversalRecursive(self, root):

        if not root:
            return []

        def _helper(node, res, depth):
            if not node:
                return
            if len(res) < depth + 1:
                res.append([])
            res[depth].append(node.val)
            _helper(node.left, res, depth + 1)
            _helper(node.right, res, depth + 1)            
            return res

        return _helper(root, [], 0)

class BST_Unittest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BST_Unittest, self).__init__(*args, **kwargs)
        self.solution = Solution()
        # create a BST
        ##        8
        ##    5         15
        ## 4    6    14    22
        self.root = TreeNode(8)
        self.root.left = TreeNode(5)
        self.root.right = TreeNode(15)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(6)
        self.root.right.left = TreeNode(14)
        self.root.right.right = TreeNode(22)

    def test_iterative_method(self):
        self.assertEqual(self.solution.levelOrderTraversalIterative(self.root), [[3], [5, 15], [4, 6, 14, 22]])

    def test_recursive_method(self):
        self.assertEqual(self.solution.levelOrderTraversalRecursive(self.root), [[8], [5, 15], [4, 6, 14, 22]])

if __name__ == '__main__':
    unittest.main()
