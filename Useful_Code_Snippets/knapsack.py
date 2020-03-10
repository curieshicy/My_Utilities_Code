class Solution:
    def knapsackProblem(self, values, weights, capacity):

        # values = [1,2,5,6]
        # weights = [2,3,4,5]
        # capacity = 8
        
        num_cols = capacity
        num_rows = len(weights)
        matrix = [[0 for i in range(num_cols + 1)] for i in range(num_rows + 1)]

        for i in range(1, num_rows + 1):
            for j in range(1, num_cols + 1):
                w = weights[i - 1]
                p = values[i - 1]
                if j - w < 0:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-w] + p)

        return matrix

values = [1,2,5,6]
weights = [2,3,4,5]
capacity = 8
solution = Solution().knapsackProblem(values, weights, capacity)

for line in solution:
    print (line)
