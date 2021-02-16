class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_sum_of_path_numbers(root):
    #FIXME this is my code, doesn't work
    def dfs(node, local_sum, total_sum):
        if not node.left and not node.right:
            total_sum += local_sum
            
        if node.left:
            dfs(node.left, node.val * 10 + node.left.val, total_sum)
            
        if node.right:
            dfs(node.left, node.val * 10 + node.right.val, total_sum)
            
        return total_sum
        
    return dfs(root, root.val, 0)
    
def find_sum_of_path_numbers(root):
    def dfs(node, path_sum):
        if not node:
            return 0
            
        path_sum = path_sum * 10 + node.val
        
        if not node.left and not node.right:
            return path_sum
            
        return dfs(node.left, path_sum) + dfs(node.right, path_sum)
        
    return dfs(root, 0)

            
def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
main()
