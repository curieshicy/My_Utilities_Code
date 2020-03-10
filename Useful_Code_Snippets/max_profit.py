def maxProfit(prices):
    res = []
    for i in range(len(prices) - 1):
        profit = max(max(prices[i+1:]) - prices[i], 0)

        res.append(profit)

    return res

## test
prices = [7, 1, 5, 3, 6, 4]
print (maxProfit(prices))
