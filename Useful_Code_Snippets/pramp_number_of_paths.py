def number_of_paths(n):
    dp = [[0 for c in range(n)] for r in range(n)]
    # fill in the bottom row
    for c in range(n):
        dp[n-1][c] = 1
        
    # fill in the table
    for r in range(n-2, -1, -1):
        for c in range(n - r - 1, n):
            dp[r][c] = dp[r][c-1] + dp[r+1][c]
    
    return dp[0][n-1]
    

print (number_of_paths(2))
