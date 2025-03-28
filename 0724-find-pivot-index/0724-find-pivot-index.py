from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Calculate the total sum of the array
        left_sum = 0  # Initialize the left sum
        
        for i in range(len(nums)):
            # Right sum is total_sum minus the left_sum and the current element
            right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i  # Found the pivot index
            
            left_sum += nums[i]  # Update left_sum for the next iteration
        
        return -1  # No pivot index found