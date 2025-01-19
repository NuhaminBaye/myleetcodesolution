from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # If we are at the edges of the array, use -inf and inf
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Check if we have partitioned correctly
            if maxX <= minY and maxY <= minX:
                # We have partitioned the array correctly
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                # We are too far on right side for partitionX. Go on left side.
                high = partitionX - 1
            else:
                # We are too far on left side for partitionX. Go on right side.
                low = partitionX + 1
        
        raise ValueError("Input arrays are not sorted or of invalid size.")

# Example usage:
sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))       # Output: 2.00000
print(sol.findMedianSortedArrays([1, 2], [3, 4]))    # Output: 2.50000