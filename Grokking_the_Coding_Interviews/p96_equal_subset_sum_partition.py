def can_partition(nums):
    total_capacity = sum(nums)
    if total_capacity % 2 == 1:
        return False
        
    capacity = total_capacity // 2
    n = len(nums)
    dp = [[0 for i in range(1 + capacity)] for j in range(1 + n)]
    for i in range(1, n + 1):
        for b in range(1, capacity + 1):
            if nums[i - 1] <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b - nums[i-1]] + nums[i-1])
            else:
                dp[i][b] = dp[i-1][b]
    return dp[n][capacity] == capacity
    
def can_partition(nums):
    # let dp[i][b] denotes whether the first i items can form a set that has a total sum equals to b
    # dp[i][b] is a boolean
    total_capacity = sum(nums)
    if total_capacity % 2 == 1:
        return False
        
    capacity = total_capacity // 2
    n = len(nums)
    dp = [[False for i in range(1 + capacity)] for j in range(n)]
    for i in range(n):
        dp[i][0] = True
        
    for b in range(1 + capacity):
        if nums[0] == b:
            dp[0][b] = True
            
    for i in range(1, n):
        for b in range(1, 1 + capacity):
            if dp[i-1][b]:
                dp[i][b] = dp[i-1][b]
            elif nums[i] <= b:
                dp[i][b] = dp[i-1][b - nums[i]]
                
    return dp[n-1][capacity]

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))
main()
