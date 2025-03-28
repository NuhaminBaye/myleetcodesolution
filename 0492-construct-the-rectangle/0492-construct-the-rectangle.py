from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Start with the largest possible width, which is the square root of the area
        import math
        width = int(math.sqrt(area))
        
        # Find the dimensions that satisfy the conditions
        while area % width != 0:
            width -= 1
        
        length = area // width
        return [length, width]