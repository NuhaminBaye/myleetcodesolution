class Solution:
    def checkRecord(self, s: str) -> bool:
        # Count the number of 'A's in the string
        absent_count = s.count('A')
        
        # Check for fewer than 2 absences
        if absent_count >= 2:
            return False
        
        # Check for 3 or more consecutive 'L's
        if 'LLL' in s:
            return False
        
        # If both conditions are satisfied
        return True

# Example usage:
solution = Solution()
print(solution.checkRecord("PPALLP"))  # Output: True
print(solution.checkRecord("PPALLL"))  # Output: False