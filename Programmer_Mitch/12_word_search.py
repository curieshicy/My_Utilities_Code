# leetcode 79

class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False
    
    def dfs(self, board, row, col, word, index):
        if len(word) == index:
            return True
            
        if row < 0 or row >= len(board) or col <0 or col >= len(board[0]) or board[row][col] != word[index]:
            return False
            
        temp = board[row][col]
        board[row][col] = ''
        
        result = False
        for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = row + x
            ny = col + y
            result =  result or self.dfs(board, nx, ny, word, index + 1)
            
        board[row][col] = temp
        
        return result
