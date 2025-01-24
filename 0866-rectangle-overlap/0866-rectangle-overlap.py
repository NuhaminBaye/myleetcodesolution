class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Check if one rectangle is to the left of the other
        if rec1[2] <= rec2[0] or rec2[2] <= rec1[0]:
            return False
        
        # Check if one rectangle is above the other
        if rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
            return False
        
        # If none of the above conditions are true, the rectangles overlap
        return True

# Example usage:
solution = Solution()
print(solution.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))  # Output: true
print(solution.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))  # Output: false
print(solution.isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3]))  # Output: false