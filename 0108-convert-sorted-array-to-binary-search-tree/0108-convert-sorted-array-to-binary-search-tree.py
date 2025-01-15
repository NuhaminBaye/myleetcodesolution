# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert_to_bst(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # Choose middle element to maintain balance
            mid = (left + right) // 2
            node = TreeNode(nums[mid])  # Create a node
            
            # Recursively build the left and right subtrees
            node.left = convert_to_bst(left, mid - 1)
            node.right = convert_to_bst(mid + 1, right)
            
            return node

        # Start the recursive function
        return convert_to_bst(0, len(nums) - 1)

# Example usage:
solution = Solution()