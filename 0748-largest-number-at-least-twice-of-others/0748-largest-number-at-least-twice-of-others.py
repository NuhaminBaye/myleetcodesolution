from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Find the maximum number and its index
        max_num = max(nums)
        max_index = nums.index(max_num)
        
        # Check if the maximum number is at least twice as much as every other number
        for i in range(len(nums)):
            if i != max_index and max_num < 2 * nums[i]:
                return -1
        
        return max_index