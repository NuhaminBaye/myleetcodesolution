class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left = 0
        minK_index = -1
        maxK_index = -1
        
        for right in range(len(nums)):
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1  # Reset the left pointer
                minK_index = -1
                maxK_index = -1
            if nums[right] == minK:
                minK_index = right
            if nums[right] == maxK:
                maxK_index = right
            
            # Both minK and maxK should be in the current window
            if minK_index != -1 and maxK_index != -1:
                # We can count all subarrays starting from 'left' to the minimum of the last indices of minK and maxK
                count += min(minK_index, maxK_index) - left + 1
        
        return count

# Example usage:
solution = Solution()