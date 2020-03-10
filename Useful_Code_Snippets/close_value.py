class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findClosestValue(self, root, target): # Node, int >>>int
        # edge case
        if not root:
            return 0

##        if not root.left:
##            return 0
##
##        if not root.right:
##            return 0
##
##        if root.val == target:
##            return root.val
##
##        if root.left.val == target:
##            return root.left.val
##
##        if root.right.val == target:
##            return root.right.val

        # none of the root.val, root.left.val nor root.right.val equals target
        
        left = self.findClosestValue(root.left, target)
        right = self.findClosestValue(root.right, target)

        print (left, right, root.val)

        return min(root.val, left, right, key = lambda t : abs(t - target))
        
## test case

##        8
##    5       14
## 4    6        22
##    8   7

root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
##root.left.left = TreeNode(4)
##root.left.right = TreeNode(6)
##root.left.right.left = TreeNode(8)
##root.left.right.right = TreeNode(7)
##root.right.right = TreeNode(22)

m = Solution().findClosestValue(root, 22)
print (m) # expect 22


        
