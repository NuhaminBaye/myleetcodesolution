from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        
        # Sum the elements at even indices
        max_sum = sum(nums[i] for i in range(0, len(nums), 2))
        
        return max_sum