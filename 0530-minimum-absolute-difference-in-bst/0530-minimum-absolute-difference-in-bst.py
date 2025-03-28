# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # List to store the values from the BST
        values = []
        
        # In-order traversal to get the values in sorted order
        def in_order_traversal(node):
            if node:
                in_order_traversal(node.left)
                values.append(node.val)
                in_order_traversal(node.right)
        
        in_order_traversal(root)
        
        # Calculate the minimum absolute difference
        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])
        
        return min_diff