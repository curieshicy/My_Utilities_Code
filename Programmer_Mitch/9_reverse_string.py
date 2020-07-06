# leetcode 344

class Solution:
    def reverseString(self, s):
        return s[::-1]
        
        
class Solution:
    def reverseString(self, s):
        return ''.join(reversed(list(s)))
    
    
class Solution:
    def reverseString(self, s):
        return_string = ''
        for i in range(len(s) - 1, -1, -1):
            return_string += s[i]
        return return_string
    
    
class Solution:
    def reverseString(self, s):
        start, end = 0, len(s) - 1
        s = list(s)
        
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -=1
        return ''.join(s)
        
    
