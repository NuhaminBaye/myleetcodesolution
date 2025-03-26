class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0  # To keep track of the maximum count of consecutive 1's
        current_count = 0  # To count the current consecutive 1's
        
        for num in nums:
            if num == 1:
                current_count += 1  # Increment count if we encounter a 1
            else:
                max_count = max(max_count, current_count)  # Update max count if we hit a 0
                current_count = 0  # Reset current count
        
        # Final check to update max_count in case the last element was a 1
        max_count = max(max_count, current_count)
        
        return max_count

# Example usage:
solution = Solution()
print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # Output: 3
print(solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # Output: 2