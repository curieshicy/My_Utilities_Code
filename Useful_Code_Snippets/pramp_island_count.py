def number_of_islands(binaryMatrix):
    if not binaryMatrix:
        return 0
        
    R, C = len(binaryMatrix), len(binaryMatrix[0])
    visited = set()
    def dfs(i, j):
        visited.add((i, j))
        for x, y in [(1, 0), (-1,0), (0, 1), (0, -1)]:
            nx = x + i
            ny = y + j
            if 0<= nx <  R and 0 <= ny < C and (nx, ny) not in visited and binaryMatrix[nx][ny] == 1:
                dfs(nx, ny)
                
    count = 0
    for i in range(R):
        for j in range(C):
            if binaryMatrix[i][j] == 1 and (i, j) not in visited:
                dfs(i,j)
                count += 1
                
    return count
    
matrix = [[0,1,0,1,0], [0,0,1,1,1], [1,0,0,1,0], [0,1,1,0,0], [1,0,1,0,1]]
print (number_of_islands(matrix))
