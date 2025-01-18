class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
           # Handle edge cases
        if dividend == 0:
            return 0
        if divisor == 0:
            raise ValueError("Divisor cannot be zero.")
        
        # Define constants for the 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values for ease of calculation
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        # The maximum bit position to check (31 bits for 32-bit integer)
        for i in range(31, -1, -1):
            # Check if divisor shifted left by i bits is less than or equal to the dividend
            if (divisor << i) <= dividend:
                dividend -= (divisor << i)  # Subtract the shifted divisor from dividend
                quotient += (1 << i)  # Add the corresponding power of two to the quotient
        
        # Apply the sign to the quotient
        if negative:
            quotient = -quotient
        
        # Clamp the result to the 32-bit signed integer range
        return min(max(INT_MIN, quotient), INT_MAX)

# Example usage:
solution = Solution()