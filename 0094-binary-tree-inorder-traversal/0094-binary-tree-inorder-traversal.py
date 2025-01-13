# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
         # This list will hold the inorder traversal result
        result = []
        
        # Define the recursive function
        def traverse(node):
            if node:
                # Traverse the left subtree
                traverse(node.left)
                # Visit the root
                result.append(node.val)
                # Traverse the right subtree
                traverse(node.right)
        
        # Start the traversal from the root
        traverse(root)
        return result