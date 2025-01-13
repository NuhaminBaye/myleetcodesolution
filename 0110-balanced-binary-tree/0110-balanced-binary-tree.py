# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            # Base case: an empty tree is balanced and has a height of 0
            if not node:
                return 0
            
            # Check the height of the left subtree
            left_height = check_balance(node.left)
            if left_height == -1:
                return -1  # Left subtree is not balanced
            
            # Check the height of the right subtree
            right_height = check_balance(node.right)
            if right_height == -1:
                return -1  # Right subtree is not balanced
            
            # If the current node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1  # Not balanced
            
            # Return the height of the tree rooted at this node
            return max(left_height, right_height) + 1

        return check_balance(root) != -1