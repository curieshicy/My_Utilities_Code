# leetcode 20
class Solution:
    def isValid(self, s):
        stack = []
        pairs = {'(': ')', '[':']', '{':'}'}
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            else:
                if not stack or stack.pop() != char:
                    return False
                    
        return not stack
