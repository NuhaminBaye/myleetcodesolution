from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

# Example usage:
solution = Solution()

# Test case 1
nums1 = [3, 2, 3]
print(solution.majorityElement(nums1))  # Output: 3

# Test case 2
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(solution.majorityElement(nums2))  # Output: 2