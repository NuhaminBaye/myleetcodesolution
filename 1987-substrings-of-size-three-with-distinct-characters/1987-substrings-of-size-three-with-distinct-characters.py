class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        
        # Iterate over the string to check each substring of length 3
        for i in range(n - 2):
            substring = s[i:i + 3]
            # Check if all characters in the substring are unique
            if len(set(substring)) == 3:
                count += 1
                
        return count

# Example usage:
solution = Solution()