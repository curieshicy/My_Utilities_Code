class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_trees_1(n):
    if n <= 0:
        return 0
        
    def dfs(arr):
        count = 0
        if not arr:
            return 1

        for num in arr:
            left_arr = [i for i in arr if i < num]
            right_arr = [i for i in arr if i > num]
            count += dfs(left_arr) * dfs(right_arr)
        
        return count
    return dfs([i for i in range(1, n + 1)])
    
def count_trees_2(n):
    def dfs(start, end):
        count = 0
        if start >= end:
            return 1
            
        for i in range(start, end + 1):
            left_count = dfs(start, i - 1)
            right_count = dfs(i + 1, end)
            count += left_count * right_count
        return count
    return dfs(1, n)
    
def count_trees_3(n):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        count = 0
        for j in range(1, i + 1):
            left = dp[j - 1]
            right = dp[i - j]
            count += left * right
        dp[i] = count
    return dp[-1]
        
        
def main():
    print("Total trees: " + str(count_trees_1(2)))
    print("Total trees: " + str(count_trees_1(3)))
    print("Total trees: " + str(count_trees_2(2)))
    print("Total trees: " + str(count_trees_2(3)))
    print("Total trees: " + str(count_trees_3(2)))
    print("Total trees: " + str(count_trees_3(3)))
main()

