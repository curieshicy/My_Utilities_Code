# leetcode 160

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
            
        a, b = headA, headB
        while a!=b:
            if not a:
                a = headB
            else:
                a = a.next
                
            if not b:
                b = headA
            else:
                b = b.next
                
        return b 
