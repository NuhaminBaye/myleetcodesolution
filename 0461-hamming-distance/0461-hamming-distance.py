class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR the two numbers to find differing bits
        xor_result = x ^ y
        
        # Count the number of 1s in the binary representation of the XOR result
        distance = 0
        while xor_result > 0:
            distance += xor_result & 1  # Check if the last bit is 1
            xor_result >>= 1  # Right shift to check the next bit
        
        return distance