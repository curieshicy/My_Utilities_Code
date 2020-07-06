# leetcode 155
class Solution:

    def __init__(self):
        self.s = []
    
    def push(self, x):
        cur_min = self.getMin()
        if not cur_min or x < cur_min:
            cur_min = x
        self.s.append((x, cur_min))
        
    def pop(self):
        self.s.pop()
        
    def top(self):
        if len(self.s) == 0:
            return None
        return self.s[-1][0]
        
    def getMin(self):
        if len(self.s) == 0:
            return None
        return self.s[-1][1]
        
