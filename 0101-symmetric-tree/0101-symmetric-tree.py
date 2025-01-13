# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Helper function to compare two trees
        def is_mirror(tree1, tree2):
            # If both nodes are None, they are symmetric
            if not tree1 and not tree2:
                return True
            # If one of the nodes is None, they are not symmetric
            if not tree1 or not tree2:
                return False
            # Check if the current nodes' values are the same
            # and recursively check their children
            return (tree1.val == tree2.val) and \
                   is_mirror(tree1.left, tree2.right) and \
                   is_mirror(tree1.right, tree2.left)
        
        # Start comparison from the root
        return is_mirror(root, root)