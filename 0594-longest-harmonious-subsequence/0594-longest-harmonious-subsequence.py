from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Count the frequency of each number
        num_count = Counter(nums)
        longest_harmonious_length = 0
        
        # Iterate through the unique numbers in the count
        for num in num_count:
            if num + 1 in num_count:
                # Calculate the length of harmonious subsequence
                current_length = num_count[num] + num_count[num + 1]
                longest_harmonious_length = max(longest_harmonious_length, current_length)
        
        return longest_harmonious_length

# Example usage:
solution = Solution()
print(solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))  # Output: 5
print(solution.findLHS([1, 2, 3, 4]))                # Output: 2
print(solution.findLHS([1, 1, 1, 1]))                # Output: 0