## code for inorder/preorder/postorder traversals of binary tree using both recursive and iterative methods.
##https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/527608/Python3-Pre-In-Post-Iteratively-Summarization

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.res = []

    def recur_traversal(self, root, mode): # return a python list

        if not root:
            return

        if mode == 'inorder':
            self.recur_traversal(root.left, mode)
            self.res.append(root.val)
            self.recur_traversal(root.right, mode)

        if mode == 'preorder':
            self.res.append(root.val)
            self.recur_traversal(root.left, mode)
            self.recur_traversal(root.right, mode)

        if mode == 'postorder':
            self.recur_traversal(root.left, mode)
            self.recur_traversal(root.right, mode)
            self.res.append(root.val)
        
        return self.res
    
    def iter_traversal(self, root, mode):
        
        if mode == "inorder": # l, R, r
            stack = []
            while root or stack:
                if root:
                    stack.append(root)
                    root = root.left

                else:
                    root = stack.pop()
                    self.res.append(root.val)
                    root = root.right

        if mode == "preorder": # R, l, r
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    self.res.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)

        if mode == "postorder": # l, r, R
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    self.res.append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                        
            self.res = self.res[::-1]
            
        return self.res
    
        
## test case
##        8
##    5         15
## 4    6    14    22

root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.left = TreeNode(14)
root.right.right = TreeNode(22)

m1 = Solution().recur_traversal(root, 'inorder')
m2 = Solution().recur_traversal(root, 'preorder')
m3 = Solution().recur_traversal(root, 'postorder')
print (m1) # [4, 5, 6, 8, 14, 15, 22]
print (m2) # [8, 5, 4, 6, 15, 14, 22]
print (m3) # [4, 6, 5, 14, 22, 15, 8]

print ("--------------------------------")

m4 = Solution().iter_traversal(root, 'inorder')
m5 = Solution().iter_traversal(root, 'preorder')
m6 = Solution().iter_traversal(root, 'postorder')
print (m4) # [4, 5, 6, 8, 14, 15, 22]
print (m5) # [8, 5, 4, 6, 15, 14, 22]
print (m6) # [4, 6, 5, 14, 22, 15, 8]

##         if mode == "preorder": # R, 1, r
##            while root or stack:
##                if root:
##                    stack.append(root)
##                    self.res.append(root.val)
##                    root = root.left
##
##                else:
##                    root = stack.pop()
##                    root = root.right          

        
