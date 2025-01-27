class Solution:
    def binaryGap(self, n: int) -> int:
           # Convert the integer to its binary representation (as a string)
        binary_rep = bin(n)[2:]  # Skip the '0b' prefix
        
        max_distance = 0  # Variable to keep track of the maximum distance
        last_position = -1  # Variable to store the position of the last '1'

        # Iterate through the binary representation
        for i, bit in enumerate(binary_rep):
            if bit == '1':
                if last_position != -1:  # If this is not the first '1'
                    # Calculate the distance from the last '1'
                    distance = i - last_position
                    max_distance = max(max_distance, distance)
                # Update the last position of '1'
                last_position = i

        return max_distance

# Example usage
solution = Solution()
print(solution.binaryGap(22))  # Output: 2
print(solution.binaryGap(8))   # Output: 0
print(solution.binaryGap(5))   # Output: 2