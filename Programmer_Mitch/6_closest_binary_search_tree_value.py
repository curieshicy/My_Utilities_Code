# leetcode 270

class Solution:
    def closestValue(self, root, target):
        return self.binary_search(root, target, root.val)
        
    def binary_search(self, node, target, closest):
        if not node:
            return closest
            
        if abs(node.val - target) < abs(closest - target):
            closest = node.val
        
        if node.val > target:
            return self.binary_search(node.left, target, closest)
        else:
            return self.binary_search(node.right, target, closest)
            
            
class Solution:
    def closestValue(self, root, target):
        closest = root.val
        
        while root:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
                
            if root.val > target:
                root = root.left
            else:
                root = root.right
                
