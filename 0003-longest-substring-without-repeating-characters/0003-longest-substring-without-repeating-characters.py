class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # Dictionary to store the last index of each character
        max_length = 0  # Variable to store the maximum length of substring
        start = 0  # Starting index of the current substring

        for i, char in enumerate(s):
            # If the character is already in the substring
            if char in char_index_map and char_index_map[char] >= start:
                # Move the start to the right of the last occurrence of the character
                start = char_index_map[char] + 1
            
            # Update the last index of the character
            char_index_map[char] = i
            
            # Calculate the maximum length
            max_length = max(max_length, i - start + 1)

        return max_length 