class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Normalize the string: convert to lowercase and filter out non-alphanumeric characters
        normalized_str = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the normalized string is the same forwards and backwards
        return normalized_str == normalized_str[::-1]

# Example usage:
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))  # Output: False
print(solution.isPalindrome(" "))  # Output: True