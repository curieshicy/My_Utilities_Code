from collections import defaultdict
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    
    def dfs(node, cur_sum, d):
        if not node:
            return 0
        
        count = 0
        cur_sum += node.val
        if cur_sum == S:
            count += 1
        count += d[cur_sum - S]
        d[cur_sum] += 1
        
        count += dfs(node.left, cur_sum, d)
        count += dfs(node.right, cur_sum, d)
        d[cur_sum] -= 1
        
        return count
        
    return dfs(root, 0, defaultdict(int))
        
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
