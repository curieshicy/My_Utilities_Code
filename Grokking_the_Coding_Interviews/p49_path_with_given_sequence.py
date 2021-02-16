class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root, sequence):
    def dfs(node, path, res):
        if not node.left and not node.right:
            res.append(path)
                
        if node.left:
            dfs(node.left, path + [node.left.val], res)
            
        if node.right:
            dfs(node.right, path + [node.right.val], res)
            
        return res
    return sequence in dfs(root, [root.val], [])
    
    
def find_path_optimal(root, sequence):
    def dfs(node, sequence, index):
        if not node:
            return False
            
        if index >= len(sequence) or sequence[index] != node.val:
            return False
        
        if not node.left and not node.right and index == len(sequence) - 1:
            return True
        return dfs(node.left, sequence, index + 1) or dfs(node.right, sequence, index + 1)
        
    if not root:
        return len(sequence) == 0
    return dfs(root, sequence, 0)
    
def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Tree has path sequence: " + str(find_path_optimal(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path_optimal(root, [1, 1, 6])))

main()
