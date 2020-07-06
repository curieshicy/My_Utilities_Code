# leetcode 26
class Solution:
    def removeDuplicates(self, A):
        if not A:
            return 0
            
        head = 0
        for i in range(len(A)):
            if A[i] != A[head]:
                head += 1
                A[head] = A[i]
                
        return head + 1
