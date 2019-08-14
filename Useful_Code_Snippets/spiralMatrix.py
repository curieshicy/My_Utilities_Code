class Solution:

    def printSpiralMatrix(self, matrix):

        direction = 0
        numRows, numCols = len(matrix), len(matrix[0])
        L, R, T, B = 0, numCols - 1, 0, numRows - 1
        res = []

        while T<=B and L<=R:

            if direction == 0:
                for _ in matrix[T][L:R+1]:
                    res.append(_)
                T += 1

            elif direction == 1:
                for i in matrix[T:B+1]:
                    res.append(i[R])
                R -= 1

            elif direction == 2:
                for i in range(R, L-1, -1):
                    res.append(matrix[B][i])
                B -= 1

            elif direction == 3:
                for i in range(B, T-1, -1):
                    res.append(matrix[i][L])
                L += 1

            direction +=1
            direction = direction %4

        return res

matrix = [[1,2,3], [4,5,6], [7,8,9]]
solution = Solution().printSpiralMatrix(matrix)
print (solution)
                        
                
