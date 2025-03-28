class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Use a set to store distinct numbers
        distinct_nums = set(nums)
        
        # Convert the set back to a sorted list
        sorted_nums = sorted(distinct_nums, reverse=True)
        
        # Return the third maximum if it exists, otherwise return the maximum
        if len(sorted_nums) >= 3:
            return sorted_nums[2]
        else:
            return sorted_nums[0]