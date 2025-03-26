from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Mark each number as negative at the index corresponding to its value
        for num in nums:
            index = abs(num) - 1  # Get the index for the value
            if nums[index] > 0:    # Check if it's already negative
                nums[index] = -nums[index]  # Mark it as seen
        
        # Collect all indices that have positive values
        missing_numbers = []
        for i in range(n):
            if nums[i] > 0:  # If the value is still positive, it's missing
                missing_numbers.append(i + 1)  # Append the missing number
        
        return missing_numbers

# Example usage:
solution = Solution()
print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # Output: [5, 6]
print(solution.findDisappearedNumbers([1, 1]))  # Output: [2]