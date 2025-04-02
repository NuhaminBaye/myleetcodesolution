from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the counter with the first word
        common_count = Counter(words[0])
        
        # Intersect the counts with each subsequent word
        for word in words[1:]:
            common_count &= Counter(word)
        
        # Expand the common characters into a list according to their counts
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result

# Example usage
solution = Solution()
print(solution.commonChars(["bella", "label", "roller"]))  # Output: ["e", "l", "l"]
print(solution.commonChars(["cool", "lock", "cook"]))      # Output: ["c", "o"]