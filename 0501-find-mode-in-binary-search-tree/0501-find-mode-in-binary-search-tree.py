from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Dictionary to hold counts of each value
        count = defaultdict(int)
        
        # In-order traversal to count occurrences of each value
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            count[node.val] += 1
            inorder(node.right)
        
        # Start in-order traversal
        inorder(root)
        
        # Find the maximum frequency
        max_count = max(count.values())
        
        # Collect all values that have the maximum frequency
        modes = [key for key, value in count.items() if value == max_count]
        
        return modes

# Example usage:
# Constructing the binary search tree for the example input [1,null,2,2]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

solution = Solution()
print(solution.findMode(root))  # Output: [2]