from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the largest index 'i' such that nums[i] < nums[i + 1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:  # If such an index exists
            # Step 2: Find the largest index 'j' such that nums[j] > nums[i]
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the sequence from nums[i + 1] to the end
        nums[i + 1:] = reversed(nums[i + 1:])

# Example usage:
solution = Solution()

# Test case 1
nums1 = [1, 2, 3]
solution.nextPermutation(nums1)
print(nums1)  # Output: [1, 3, 2]

# Test case 2
nums2 = [3, 2, 1]
solution.nextPermutation(nums2)
print(nums2)  # Output: [1, 2, 3]

# Test case 3
nums3 = [1, 1, 5]
solution.nextPermutation(nums3)
print(nums3)  # Output: [1, 5, 1]
        