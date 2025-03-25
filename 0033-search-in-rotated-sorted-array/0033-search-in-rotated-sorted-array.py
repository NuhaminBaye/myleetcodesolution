class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # Determine which side is sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the left half
                else:
                    left = mid + 1  # Target is in the right half
            else:  # Right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target is in the right half
                else:
                    right = mid - 1  # Target is in the left half
        
        return -1  # Target not found

# Example usage:
solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))  # Output: 4
print(solution.search([4,5,6,7,0,1,2], 3))  # Output: -1
print(solution.search([1], 0))                # Output: -1