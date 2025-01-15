# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If left child is None, go down the right subtree
        if not root.left:
            return self.minDepth(root.right) + 1
        
        # If right child is None, go down the left subtree
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # If both children exist, find the minimum depth of both subtrees
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        return min(left_depth, right_depth) + 1

# Example usage:
solution = Solution()
# Constructing the example tree [3,9,20,null,null,15,7]