class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine the sign of x
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        
        # Reverse the digits
        reversed_x = 0
        while x_abs:
            digit = x_abs % 10  # Get the last digit
            x_abs //= 10  # Remove the last digit
            
            # Check for overflow before multiplying and adding
            if (reversed_x > (INT_MAX - digit) // 10):
                return 0  # Return 0 if it overflows
            
            reversed_x = reversed_x * 10 + digit
        
        # Apply the sign to the reversed number
        reversed_x *= sign
        
        # Check if the final result is within the 32-bit integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x 