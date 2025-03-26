from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create an empty set to store seen numbers
        
        for num in nums:
            if num in seen:  # Check if the number has already been seen
                return True  # If it has, return True
            seen.add(num)  # Otherwise, add the number to the set
        
        return False  # If no duplicates were found, return False

# Example usage:
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))  # Output: True
print(solution.containsDuplicate([1, 2, 3, 4]))  # Output: False
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True