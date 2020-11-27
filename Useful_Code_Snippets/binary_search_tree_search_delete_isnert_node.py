'''
    Delete a node in binary search tree
'''
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def find_successor(node):
            node = node.right
            while node.left:
                node = node.left
            return node.val
        
        def find_predecessor(node):
            node = node.left
            while node.right:
                node = node.right
            return node.val
        
        def delete_node(node, key):
            if not node:
                return None
        
            if node.val < key:
                node.right = delete_node(node.right, key)
            elif node.val > key:
                node.left = delete_node(node.left, key)
            else:
                if not node.left and not node.right:
                    node = None
                    
                elif node.right:
                    val = find_successor(node)
                    node.val = val
                    node.right = delete_node(node.right, val)
                else:
                    val = find_predecessor(node)
                    node.val = val
                    node.left = delete_node(node.left, val)
            return node
        
        return delete_node(root, key)

'''
    Insert a node into binary search tree
'''

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        node = root
        while node:
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left

'''
    Search a node in binary search tree
'''
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if val == root.val:
                return root
            
            elif val < root.val:
                root = root.left
            
            else:
                root = root.right
                
        return None

    def closestValue(self, root: TreeNode, target: float) -> int:
        
        # track diff and res
        # termination conditions are either hitting an empty node or target equates one of the nodes
        # iteratively update the root, and make the comparison with the previous (diff, res)
        # O(logN) time, O(1) space
        
        diff = float('inf')
        res = root.val
        
        while root:
            if abs(root.val - target) < diff:
                diff = abs(root.val - target)
                res = root.val
                
            if target < root.val:
                root = root.left
                
            elif target > root.val:
                root = root.right
                
            elif target == root.val:
                return root.val
            
        return res 

        
