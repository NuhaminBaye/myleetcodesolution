class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the array
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1  # Initialize two pointers
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Move left pointer to the right to increase the sum
                elif total > 0:
                    right -= 1  # Move right pointer to the left to decrease the sum
                else:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        return result

# Example usage:
solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(solution.threeSum([0, 1, 1]))                # Output: []
print(solution.threeSum([0, 0, 0]))                # Output: [[0, 0, 0]]
                

        