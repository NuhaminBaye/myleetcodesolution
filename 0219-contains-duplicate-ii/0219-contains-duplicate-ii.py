from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}  # Dictionary to store the last index of each number
        
        for i, num in enumerate(nums):
            if num in index_map:
                # Check if the current index and the last index are within k
                if i - index_map[num] <= k:
                    return True  # Found a duplicate within the range
            index_map[num] = i  # Update the last index of the current number
        
        return False  # No duplicates found within the range

# Example usage:
solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: True
print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))  # Output: True
print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Output: False