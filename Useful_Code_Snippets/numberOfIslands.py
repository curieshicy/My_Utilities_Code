class Solution:

    def numberOfIslands(self, grid):

        if not grid:
            return 0

        r, c = len(grid), len(grid[0])
        visited = set()
        count = 0
        
        def dfs(i,j):
            visited.add((i,j))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for direction in directions:
                nx, ny = i + direction[0], j + direction[1]
                if 0<=nx<r and 0<=ny<c and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    dfs(nx,ny)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i,j)
                    count += 1

        return count


import unittest
class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()
        self.map = [[1, 1, 0], [0, 1, 1], [0, 1, 1]]

    def testNumberOfIslands(self):
        self.assertEqual(self.solution.numberOfIslands(self.map), 1)

if __name__ == '__main__':
    unittest.main()
        
