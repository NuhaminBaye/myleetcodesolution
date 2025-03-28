# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # Initialize the first and second minimum values
        first_min = root.val
        second_min = float('inf')
        
        # Helper function for DFS traversal
        def dfs(node):
            nonlocal second_min
            if not node:
                return
            
            # If the current node's value is greater than the first minimum
            if first_min < node.val < second_min:
                second_min = node.val
            
            # Continue DFS on left and right children
            dfs(node.left)
            dfs(node.right)
        
        # Start DFS traversal from the root node
        dfs(root)
        
        # If second_min was not updated, return -1
        return second_min if second_min < float('inf') else -1