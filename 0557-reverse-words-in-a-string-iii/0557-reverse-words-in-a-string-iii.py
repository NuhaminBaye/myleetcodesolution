class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split(" ")
        
        # Reverse each word
        reversed_words = [word[::-1] for word in words]
        
        # Join the reversed words back into a single string
        return " ".join(reversed_words)

# Example usage:
solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))  # Output: "s'teL ekat edoCteeL tsetnoc"
print(solution.reverseWords("Mr Ding"))                       # Output: "rM gniD"