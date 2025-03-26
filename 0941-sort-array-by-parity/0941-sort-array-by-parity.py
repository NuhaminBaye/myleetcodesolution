from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Create two separate lists for even and odd numbers
        even = [num for num in nums if num % 2 == 0]
        odd = [num for num in nums if num % 2 != 0]
        
        # Concatenate even and odd lists
        return even + odd