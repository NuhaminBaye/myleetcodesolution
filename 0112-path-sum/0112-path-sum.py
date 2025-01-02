# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If the current node is None, return False (base case)
        if not root:
            return False
        
        # If we reach a leaf node, check if the remaining sum equals the leaf's value
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Subtract the current node's value from the target sum and explore the left and right children
        targetSum -= root.val
        
        return (self.hasPathSum(root.left, targetSum) or 
                self.hasPathSum(root.right, targetSum))

# Example usage:
# Constructing the binary tree for testing
root1 = TreeNode(5)
root1.left = TreeNode(4)
root1.right = TreeNode(8)
root1.left.left = TreeNode(11)
root1.left.left.left = TreeNode(7)
root1.left.left.right = TreeNode(2)
root1.right.left = TreeNode(13)
root1.right.right = TreeNode(4)
root1.right.right.right = TreeNode(1)

solution = Solution()
print(solution.hasPathSum(root1, 22))  # Output: True

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(solution.hasPathSum(root2, 5))  # Output: False

root3 = None
print(solution.hasPathSum(root3, 0))  # Output: False