class Solution:
    def countSegments(self, s: str) -> int:
        # Split the string by spaces and filter out empty segments
        segments = s.split()
        return len(segments)

# Example usage:
solution = Solution()
print(solution.countSegments("Hello, my name is John"))  # Output: 5
print(solution.countSegments("Hello"))                    # Output: 1