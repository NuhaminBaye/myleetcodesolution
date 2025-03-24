class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Get the length of the string
        n = len(s)
        
        # Check for possible substring lengths
        for i in range(1, n // 2 + 1):
            # If the current length is a divisor of n
            if n % i == 0:
                # Construct the substring by repeating
                substring = s[:i] * (n // i)
                # Check if the constructed string matches the original
                if substring == s:
                    return True
        
        return False

# Example usage:
solution = Solution()
print(solution.repeatedSubstringPattern("abab"))         # Output: True
print(solution.repeatedSubstringPattern("aba"))          # Output: False
print(solution.repeatedSubstringPattern("abcabcabcabc"))  # Output: True