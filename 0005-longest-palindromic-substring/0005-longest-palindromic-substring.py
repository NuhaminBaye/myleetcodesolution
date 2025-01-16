class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
           return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # Expand around the center for odd-length palindromes
            len1 = self.expandAroundCenter(s, i, i)
            # Expand around the center for even-length palindromes
            len2 = self.expandAroundCenter(s, i, i + 1)
            # Get the maximum length found
            max_len = max(len1, len2)
            
            if max_len > end - start:
                # Update start and end indices
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Length of the palindrome