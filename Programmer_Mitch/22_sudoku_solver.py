# leetcode 37

class Solution:
    def solveSudoku(self, board):
        if not board or len(board) == 0:
            return
            
        self.solve(board)
        

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    for c in '123456789':
                        if self.is_valid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                                
                    return False
        return True
        
    
    def is_valid(self, board, row, col, c):
        for num in range(0,9):
            if board[row][num] == c:
                return False
            if board[num][col] == c:
                return False
            if board[3 * int(row / 3) + int(num / 3)][3 * int(col/3) + num % 3] == c:
                return False
        return True
            
            
