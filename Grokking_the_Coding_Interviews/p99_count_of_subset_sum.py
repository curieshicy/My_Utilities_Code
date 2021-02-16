def count_subsets(nums, summation):
    # let dp[i][b] denotes number of ways to sum up to b using the first i items
    n = len(nums)
    capacity = summation
    dp = [[0 for i in range(1 + capacity)] for j in range(n)]
    
    for i in range(n):
        dp[i][0] = 1
    
    for b in range(1, 1 + capacity):
        if nums[0] == b:
            dp[0][b] = 1
            
    for i in range(1, n):
        for b in range(1, 1 + capacity):
            dp[i][b] = dp[i-1][b]
            if nums[i] <= b:
                dp[i][b] += dp[i-1][b - nums[i]]
                
    return dp[n-1][capacity]

def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
