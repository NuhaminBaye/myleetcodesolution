class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
          # Sort the array to use two-pointer technique
        nums.sort()
        closest_sum = float('inf')  # Initialize closest sum as infinity

        # Iterate through the array
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if the current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers based on the comparison of current_sum and target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If current_sum is exactly the target, return it
                    return current_sum
        
        return closest_sum

# Example usage:
sol = Solution()