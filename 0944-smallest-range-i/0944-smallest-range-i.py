from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # Find the maximum and minimum values in the array
        max_num = max(nums)
        min_num = min(nums)
        
        # Calculate the new minimum and maximum after applying the operations
        new_min = min_num + k
        new_max = max_num - k
        
        # The minimum score is the difference between the new max and new min
        # If the new_max is less than new_min, the score is 0
        return max(0, new_max - new_min)