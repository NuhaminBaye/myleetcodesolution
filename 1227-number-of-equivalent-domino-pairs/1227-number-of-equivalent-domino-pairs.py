from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        
        # Count each domino in a normalized way (sorted representation)
        for a, b in dominoes:
            # Normalize the domino representation by sorting the pair
            normalized = tuple(sorted((a, b)))
            count[normalized] += 1
        
        # Calculate the number of equivalent pairs
        total_pairs = 0
        for c in count.values():
            if c > 1:
                # If there are c occurrences, we can choose 2 out of c
                total_pairs += (c * (c - 1)) // 2
        
        return total_pairs

# Example usage:
solution = Solution()
print(solution.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))  # Output: 1
print(solution.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))  # Output: 3