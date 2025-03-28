from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        # If the original color is the same as the new color, no need to do anything
        if original_color == color:
            return image
        
        # Get the dimensions of the image
        rows, cols = len(image), len(image[0])
        
        # Define the DFS function
        def dfs(r: int, c: int):
            # Check if the current position is out of bounds or not the original color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            
            # Change the color
            image[r][c] = color
            
            # Recursive calls for the four adjacent pixels
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        # Start the DFS from the starting pixel
        dfs(sr, sc)
        
        return image