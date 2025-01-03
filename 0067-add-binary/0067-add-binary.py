class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize variables
        result = []
        carry = 0
        
        # Make sure a is the longer string
        if len(a) < len(b):
            a, b = b, a
            
        # Reverse both strings for easier addition from the least significant bit
        a = a[::-1]
        b = b[::-1]
        
        # Loop through the length of the longer string
        for i in range(len(a)):
            # Get the current bits and add them along with the carry
            bit_a = int(a[i])  # Convert current bit of a to integer
            bit_b = int(b[i]) if i < len(b) else 0  # Convert current bit of b to integer, or use 0
            total = bit_a + bit_b + carry
            
            # Determine the bit to add to the result and the new carry
            result_bit = total % 2
            carry = total // 2
            
            # Append the result bit
            result.append(str(result_bit))
        
        # If there's a carry left, append it
        if carry:
            result.append(str(carry))
        
        # Reverse the result to get the final binary string and return it
        return ''.join(result[::-1])

# Example usage:
solution = Solution()
print(solution.addBinary("11", "1"))      # Output: "100"
print(solution.addBinary("1010", "1011"))  # Output: "10101"
    