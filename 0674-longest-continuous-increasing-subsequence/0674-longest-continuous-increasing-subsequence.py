from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_length = 1  # At least one element is an increasing subsequence
        current_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1  # Reset for the next potential subsequence
        
        # Final check to update max_length if the longest subsequence ends at the last element
        max_length = max(max_length, current_length)
        
        return max_length