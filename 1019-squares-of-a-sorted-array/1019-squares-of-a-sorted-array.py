from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # Create an array to hold the squared values
        left, right = 0, n - 1  # Initialize two pointers
        
        for i in range(n - 1, -1, -1):
            left_val = nums[left] ** 2
            right_val = nums[right] ** 2
            
            if left_val > right_val:
                result[i] = left_val
                left += 1
            else:
                result[i] = right_val
                right -= 1
        
        return result