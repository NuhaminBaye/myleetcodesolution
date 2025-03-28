from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:  # Check if it's land
                    # Each land cell contributes 4 sides
                    perimeter += 4
                    
                    # Check for adjacent land cells and subtract from perimeter
                    if i > 0 and grid[i - 1][j] == 1:  # Check above
                        perimeter -= 1
                    if i < rows - 1 and grid[i + 1][j] == 1:  # Check below
                        perimeter -= 1
                    if j > 0 and grid[i][j - 1] == 1:  # Check left
                        perimeter -= 1
                    if j < cols - 1 and grid[i][j + 1] == 1:  # Check right
                        perimeter -= 1
        
        return perimeter