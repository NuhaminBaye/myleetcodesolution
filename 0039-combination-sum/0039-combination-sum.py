from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))  # Found a valid combination
                return
            elif remaining < 0:
                return  # Exceeded the target
            
            for i in range(start, len(candidates)):
                combination.append(candidates[i])  # Choose the current candidate
                backtrack(remaining - candidates[i], combination, i)  # Not i + 1 because we can reuse the same element
                combination.pop()  # Backtrack
        
        backtrack(target, [], 0)
        return result

# Example usage:
solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]
print(solution.combinationSum([2, 3, 5], 8))     # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(solution.combinationSum([2], 1))            # Output: []