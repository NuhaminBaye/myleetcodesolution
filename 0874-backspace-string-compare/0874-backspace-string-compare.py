class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_valid_index(string: str, index: int) -> int:
            skip = 0
            while index >= 0:
                if string[index] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break
                index -= 1
            return index
        
        index_s = len(s) - 1
        index_t = len(t) - 1
        
        while index_s >= 0 or index_t >= 0:
            next_s = get_next_valid_index(s, index_s)
            next_t = get_next_valid_index(t, index_t)
            
            # If both indices are out of bounds, they are equal
            if next_s < 0 and next_t < 0:
                return True
            
            # If one is out of bounds, they are not equal
            if next_s < 0 or next_t < 0:
                return False
            
            # Compare characters
            if s[next_s] != t[next_t]:
                return False
            
            # Move to the next valid character
            index_s = next_s - 1
            index_t = next_t - 1
        
        return True

# Example usage:
solution = Solution()

# Test case 1
print(solution.backspaceCompare("ab#c", "ad#c"))  # Output: True

# Test case 2
print(solution.backspaceCompare("ab##", "c#d#"))  # Output: True

# Test case 3
print(solution.backspaceCompare("a#c", "b"))      # Output: False 