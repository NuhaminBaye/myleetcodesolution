class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Convert the string to a list to allow modification
        s_list = list(s)
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move the left pointer to the next letter
            while left < right and not s_list[left].isalpha():
                left += 1
            # Move the right pointer to the previous letter
            while left < right and not s_list[right].isalpha():
                right -= 1
            
            # Swap the letters
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        # Join the list back into a string and return
        return ''.join(s_list)

# Example usage:
if __name__ == "__main__":
    solution = Solution()