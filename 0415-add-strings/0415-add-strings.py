class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers for both strings
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        # Loop until both strings are processed
        while i >= 0 or j >= 0 or carry:
            # Get the current digits or 0 if the pointer is out of bounds
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # Calculate the sum of the digits and carry
            total = digit1 + digit2 + carry
            carry = total // 10  # Update carry for the next iteration
            result.append(total % 10)  # Append the last digit of the total
            
            # Move to the next digits
            i -= 1
            j -= 1
        
        # The result list contains the digits in reverse order
        return ''.join(str(x) for x in reversed(result))

# Example usage:
solution = Solution()