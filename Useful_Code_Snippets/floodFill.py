class Solution:

    def floodFillDFS(self, image, sr, sc, newColor):
        visited = set()
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        self.dfs(image, sr, sc, newColor, oldColor, visited)
        return image

    def dfs(self, image, i, j, newColor, oldColor, visited):

        if (i,j) not in visited:
            visited.add((i,j))

            image[i][j] = newColor
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for direction in directions:
                nx = direction[0] + i
                ny = direction[1] + j
                if 0<=nx<len(image) and 0<=ny<len(image[0]) and image[nx][ny] == oldColor:
                    image[nx][ny] = newColor
                    self.dfs(image, nx, ny, newColor, oldColor, visited)    

    def floodFillBFS(self, image, sr, sc, newColor):
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        from collections import deque
        queue = deque([(sr, sc)])
        visited = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            pos = queue.popleft()
            if pos in visited:
                continue

            if pos not in visited:
                visited.add(pos)

            image[pos[0]][pos[1]] = newColor
            for direction in directions:
                nx = direction[0] + pos[0]
                ny = direction[1] + pos[1]
                if 0<=nx<len(image) and 0<=ny<len(image[0]) and image[nx][ny] == oldColor:
                    image[nx][ny] = newColor
                    queue.append((nx, ny))

        return image
                

import unittest
class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()
        self.image = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        self.sr, self.sc = 1, 1
        self.newColor = 2

    def testFloodFillDFS(self):
        self.assertEqual(self.solution.floodFillDFS(self.image,
                                                    self.sr,
                                                    self.sc,
                                                    self.newColor),
                         [[0, 0, 0], [0, 2, 0], [2, 2, 2]])
        
    def testFloodFillBFS(self):
        self.assertEqual(self.solution.floodFillBFS(self.image,
                                                    self.sr,
                                                    self.sc,
                                                    self.newColor),
                         [[0, 0, 0], [0, 2, 0], [2, 2, 2]])


if __name__ == '__main__':
    unittest.main()


        
