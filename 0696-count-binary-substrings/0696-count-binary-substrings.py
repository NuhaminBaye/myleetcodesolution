class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Initialize a list to store the lengths of consecutive groups
        groups = []
        
        # Count consecutive characters and form groups
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)  # Append the last group
        
        # Count valid substrings
        result = 0
        for i in range(1, len(groups)):
            result += min(groups[i - 1], groups[i])  # The number of valid substrings
        
        return result