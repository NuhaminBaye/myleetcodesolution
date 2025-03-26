class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:  # Handle the case for zero
            return "0"
        
        negative = num < 0  # Check if the number is negative
        num = abs(num)  # Work with the absolute value of the number
        base7 = []
        
        while num > 0:
            base7.append(str(num % 7))  # Get the remainder and convert to string
            num //= 7  # Divide the number by 7
        
        if negative:
            base7.append('-')  # Add the negative sign if the number was negative
        
        return ''.join(reversed(base7))  # Reverse the list and join to get the final string

# Example usage:
solution = Solution()
print(solution.convertToBase7(100))  # Output: "202"
print(solution.convertToBase7(-7))    # Output: "-10"