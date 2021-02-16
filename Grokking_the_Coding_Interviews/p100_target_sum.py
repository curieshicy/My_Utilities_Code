def find_target_subsets(nums, s):
    if sum(nums) < s:
        return 0
    total_sum = sum(nums)
    target = s + total_sum
    if target % 2 == 1:
        return 0
    capacity = target // 2
    
    n = len(nums)
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
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))
main()
