from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Count the frequency of each character in both strings
        return Counter(s) == Counter(t)

# Example usage:
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))          # Output: False