class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
         # Create a map to hold the next greater elements
        next_greater = {}
        stack = []
        
        # Iterate through nums2 to fill the next_greater map
        for num in nums2:
            while stack and stack[-1] < num:
                # Pop from stack and set the next greater element
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # Fill in the next greater elements for nums1
        result = []
        for num in nums1:
            result.append(next_greater.get(num, -1))
        
        return result

# Example usage:
solution = Solution()
print(solution.nextGreaterElement([4,1,2], [1,3,4,2]))  # Output: [-1, 3, -1]
print(solution.nextGreaterElement([2,4], [1,2,3,4]))     # Output: [3, -1]