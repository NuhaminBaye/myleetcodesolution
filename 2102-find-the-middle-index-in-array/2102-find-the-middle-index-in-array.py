class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for index in range(len(nums)):
            # Calculate the right sum by subtracting the left sum and the current element
            right_sum = total_sum - left_sum - nums[index]
            
            if left_sum == right_sum:
                return index
            
            # Update the left sum for the next iteration
            left_sum += nums[index]
        
        return -1

# Example usage:
solution = Solution()