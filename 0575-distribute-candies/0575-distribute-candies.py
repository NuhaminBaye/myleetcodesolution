from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Calculate the maximum number of candies Alice can eat
        max_candies = len(candyType) // 2
        
        # Get the unique types of candies
        unique_candies = len(set(candyType))
        
        # The result is the minimum of unique types and max_candies
        return min(unique_candies, max_candies)

# Example usage:
solution = Solution()
print(solution.distributeCandies([1, 1, 2, 2, 3, 3]))  # Output: 3
print(solution.distributeCandies([1, 1, 2, 3]))        # Output: 2
print(solution.distributeCandies([6, 6, 6, 6]))        # Output: 1