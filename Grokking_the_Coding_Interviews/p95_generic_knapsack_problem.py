def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    dp = [[0 for i in range(1 + capacity)] for j in range(1 + n)]
    for i in range(1, 1 + n):
        for b in range(1, 1 + capacity):
            if weights[i-1] <= b:
                dp[i][b] = max(profits[i-1] + dp[i-1][b - weights[i-1]], dp[i-1][b])
            else:
                dp[i][b] = dp[i-1][b]
                
    return dp[n][capacity]

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
main()
