class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_paths(root):
    def dfs(node, path, res):
        if not node.left and not node.right:
            res.append(path)
        if node.left:
            dfs(node.left, path + [node.left.val], res)
        if node.right:
            dfs(node.right, path + [node.right.val], res)
        return res
        
    return dfs(root, [root.val], [])


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(find_paths(root))
    
main()
