from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n  # If no operations, all cells remain 0
        
        # Initialize min_row and min_col to their maximum possible values
        min_row = m
        min_col = n
        
        # Find the minimum dimensions from the operations
        for a, b in ops:
            min_row = min(min_row, a)
            min_col = min(min_col, b)
        
        # The number of maximum integers will be the product of the minimum dimensions
        return min_row * min_col