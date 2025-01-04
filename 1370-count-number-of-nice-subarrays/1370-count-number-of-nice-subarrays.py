class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(k: int) -> int:
            count = 0
            left = 0
            for right in range(len(nums)):
                # If the current number is odd, decrement k
                if nums[right] % 2 == 1:
                    k -= 1
                # If we have more than k odd numbers, move the left pointer
                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1
                # Count the number of valid subarrays ending at right
                count += right - left + 1
            return count
        
        # Use the helper function to count subarrays with at most k
        return atMostK(k) - atMostK(k - 1)

# Example usage:
solution = Solution()