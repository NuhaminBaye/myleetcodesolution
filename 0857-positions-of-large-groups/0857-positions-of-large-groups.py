class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        n = len(s)
        i = 0
        
        while i < n:
            start = i
            # Move i forward while the next character is the same
            while i < n - 1 and s[i] == s[i + 1]:
                i += 1
            end = i
            
            # Check if the group size is large
            if end - start + 1 >= 3:
                result.append([start, end])
            
            # Move to the next character
            i += 1
        
        return result

# Example usage:
solution = Solution()
print(solution.largeGroupPositions("abbxxxxzzy"))  # Output: [[3, 6]]
print(solution.largeGroupPositions("abc"))          # Output: []
print(solution.largeGroupPositions("abcdddeeeeaabbbcd"))  # Output: [[3, 5], [6, 9], [12, 14]]