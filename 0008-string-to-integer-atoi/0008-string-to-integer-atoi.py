class Solution:
    def myAtoi(self, s: str) -> int:
        # Define the boundaries for the 32-bit signed integer
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Initialize index and sign
        index = 0
        sign = 1
        result = 0
        
        # Step 1: Ignore leading whitespace
        while index < len(s) and s[index] == ' ':
            index += 1
        
        # Step 2: Check for sign
        if index < len(s) and (s[index] == '+' or s[index] == '-'):
            sign = -1 if s[index] == '-' else 1
            index += 1
        
        # Step 3: Read the integer
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            # Check for overflow before adding the digit
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            index += 1
        
        return sign * result

# Example Usage
solution = Solution()

# Test cases
print(solution.myAtoi("42"))          # Output: 42
print(solution.myAtoi("   -042"))     # Output: -42
print(solution.myAtoi("1337c0d3"))    # Output: 1337
print(solution.myAtoi("0-1"))         # Output: 0
print(solution.myAtoi("words and 987")) # Output: 0