def can_partition(nums, sum):
    n = len(nums)
    capacity = sum
    
    dp = [[0 for i in range(1 + capacity)] for j in range(1 + n)]
    for i in range(1, 1 + n):
        for b in range(1, 1 + capacity):
            if nums[i-1] <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b - nums[i-1]] + nums[i-1])
            else:
                dp[i][b] = dp[i-1][b]
    
    for i in range(1 + n):
        for j in range(1 + capacity):
            if dp[i][j] == sum:
                return True
    return False

def can_partition(nums, sum):
    n = len(nums)
    capacity = sum
    # let dp[i][b] denotes if there exists a subset of first i items that makes b capacity
    dp = [[False for i in range(1 + capacity)] for j in range(n)]
    
    for i in range(n):
        dp[i][0] = True
        
    for b in range(1, 1 + capacity):
        if nums[0] == b:
            dp[0][b] = True
            
    for i in range(n):
        for b in range(1, 1 + capacity):
            if dp[i-1][b]:
                dp[i][b] = dp[i-1][b]
            elif nums[i] <= b:
                dp[i][b] = dp[i-1][b - nums[i]]
                
    return dp[n-1][capacity]
    

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
