class Solution:
    def bfsTreePath(self, root):
        if not root:
            return []

        from collections import deque
        queue = deque([(root, str(root.val))])
        res = []
        while queue:
            level_path = ''
            for i in range(len(queue)):
                node, path = queue.popleft()
                level_path += path
                
                if node.left:
                    queue.append((node.left, str(node.left.val)))

                if node.right:
                    queue.append((node.right, str(node.right.val)))

            res.append(level_path)
        return res
            

    def dfsTreePath(self, root):
        if not root:
            return []

        res = []
        self.dfs(root, str(root.val), res)
        return res
        
    def dfs(self, node, path, res):
        if not node.left and not node.right:
            res.append(path)

        if node.left:
            self.dfs(node.left, path + str(node.left.val), res)

        if node.right:
            self.dfs(node.right, path + str(node.right.val), res)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# construct a tree
#            1
#          2   3
#        4  5    6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# test
bfs = Solution().bfsTreePath(root)
dfs = Solution().dfsTreePath(root)
print (bfs)
print (dfs)

