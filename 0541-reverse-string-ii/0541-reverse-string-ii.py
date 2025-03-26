class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        n = len(s)
        
        for i in range(0, n, 2 * k):
            # Get the substring for the current segment
            segment = s[i:i + 2 * k]
            # Reverse the first k characters
            first_part = segment[:k][::-1]
            # The second part remains unchanged
            second_part = segment[k:2 * k]
            # Append both parts to the result
            result.append(first_part + second_part)
        
        return ''.join(result)

# Example usage:
solution = Solution()
print(solution.reverseStr("abcdefg", 2))  # Output: "bacdfeg"
print(solution.reverseStr("abcd", 2))     # Output: "bacd"