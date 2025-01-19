
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._preorder_helper(root, result)
        return result
    
    def _preorder_helper(self, node: Optional[TreeNode], result: List[int]):
        if node:
            result.append(node.val)  # Visit the root
            self._preorder_helper(node.left, result)  # Traverse left subtree
            self._preorder_helper(node.right, result)  # Traverse right subtree

# Example usage:
# Constructing a binary tree:
#         1
#          \
#           2
#          /
#         3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.preorderTraversal(root))  # Output: [1, 2, 3]