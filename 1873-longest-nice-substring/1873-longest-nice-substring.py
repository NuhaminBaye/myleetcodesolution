class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        max_len = 0
        longest_nice_substring = ""
        
        # Iterate through all possible substrings
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if self.is_nice(substring):
                    if len(substring) > max_len:
                        max_len = len(substring)
                        longest_nice_substring = substring
        
        return longest_nice_substring

    def is_nice(self, substring: str) -> bool:
        # Create a set to track the characters
        char_set = set(substring)
        
        # Check if for every character its counterpart exists
        for char in char_set:
            if char.lower() not in char_set or char.upper() not in char_set:
                return False
        
        return True

# Example usage:
solution = Solution()