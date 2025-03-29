class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove dashes and convert to uppercase
        s = s.replace('-', '').upper()
        
        # Determine the length of the first group
        first_group_length = len(s) % k or k
        
        # Start with the first group
        formatted_key = s[:first_group_length]
        
        # Add remaining groups
        for i in range(first_group_length, len(s), k):
            formatted_key += '-' + s[i:i + k]
        
        return formatted_key

# Example usage:
solution = Solution()
print(solution.licenseKeyFormatting("5F3Z-2e-9-w", 4))  # Output: "5F3Z-2E9W"
print(solution.licenseKeyFormatting("2-5g-3-J", 2))      # Output: "2-5G-3J"