class Solution:
    def arrangeCoins(self, n: int) -> int:
       # Use a binary search to find the number of complete rows
        left, right = 0, n
        
        while left <= right:
            mid = (left + right) // 2
            # Calculate the total coins needed for mid complete rows
            total_coins = (mid * (mid + 1)) // 2
            
            if total_coins == n:
                return mid  # Found the exact number of rows
            elif total_coins < n:
                left = mid + 1  # We can try for more rows
            else:
                right = mid - 1  # We need to try fewer rows
        
        return right  # The last valid mid value

# Example usage:
solution = Solution()
print(solution.arrangeCoins(5))  # Output: 2
print(solution.arrangeCoins(8))  # Output: 3 