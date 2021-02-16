class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_unique_trees(n):
    def num_trees(arr):
        res = 0
        if not arr:
            return 1
        for num in arr:
            left = [i for i in arr if i < num ]
            right = [i for i in arr if i > num]
            res += num_trees(left) * num_trees(right)
        return res
    return num_trees([i for i in range(1, n + 1)])
    
print (find_unique_trees(2))
print (find_unique_trees(3))

def find_unique_trees(n):
    if n <= 0:
        return []
    
    def dfs(start, end):
        result = []
        if start > end:
            result.append(None)
            return result
            
        for num in range(start, end + 1):
            left_subtrees = dfs(start, num - 1)
            right_subtrees = dfs(num + 1, end)
            for left_tree in left_subtrees:
                for right_tree in right_subtrees:
                    root = TreeNode(num)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)
                    
        return result
    
    return dfs(1, n)

def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))
main()
