class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Prepare a result array to store intermediate results
        result = [0] * (len(num1) + len(num2))
        
        # Reverse the strings to facilitate position calculations
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                # Multiply digits and add to the corresponding position in the result
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                result[i + j] += product  # Add to the current position
                
                # Handle carry
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # Remove leading zeros and convert result back to string
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        return ''.join(map(str, result[::-1]))

# Example usage:
solution = Solution()
print(solution.multiply("2", "3"))        # Output: "6"
print(solution.multiply("123", "456"))    # Output: "56088"