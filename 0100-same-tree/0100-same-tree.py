# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
         # Both trees are empty
        if not p and not q:
            return True
        # One of the trees is empty, and the other is not
        if not p or not q:
            return False
        # Both nodes have the same value, check the left and right subtrees
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)