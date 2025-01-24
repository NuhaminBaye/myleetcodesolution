# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: if the root is None, return None
        if root is None:
            return None
        
        # If the current node's value matches the target value, return the node
        if root.val == val:
            return root
        
        # Since this is a BST, we can decide to go left or right
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# Example usage:
# Constructing the BST from example 1: [4,2,7,1,3]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
result = solution.searchBST(root, 2)