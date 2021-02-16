def can_partition(nums):
    total_capacity = sum(nums)
    capacity = total_capacity // 2
    
    n = len(nums)
    dp = [[0 for i in range(1 + capacity)] for j in range(1 + n)]
    for i in range(1, 1 + n):
        for b in range(1, 1 + capacity):
            if nums[i - 1] <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b - nums[i-1]] + nums[i-1])
            else:
                dp[i][b] = dp[i-1][b]
    
    max_val = dp[n][capacity]
    remainder = total_capacity - max_val
    diff = abs(max_val - remainder)
    return diff


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
