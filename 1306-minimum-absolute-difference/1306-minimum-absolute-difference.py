from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initialize variables to track minimum difference and result pairs
        min_diff = float('inf')
        result = []
        
        # Step 3: Find the minimum absolute difference
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i + 1]]]
            elif diff == min_diff:
                result.append([arr[i], arr[i + 1]])
        
        return result

# Example usage:
solution = Solution()
print(solution.minimumAbsDifference([4,2,1,3]))  # Output: [[1,2],[2,3],[3,4]]
print(solution.minimumAbsDifference([1,3,6,10,15]))  # Output: [[1,3]]
print(solution.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))  # Output: [[-14,-10],[19,23],[23,27]]