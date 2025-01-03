class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = 0
        for i in range(32):
            # Shift reversed_num left by 1 to make space for the next bit
            reversed_num <<= 1
            # Add the least significant bit of n to reversed_num
            reversed_num |= (n & 1)
            # Shift n right by 1 to process the next bit
            n >>= 1
        return reversed_num

# Example usage:
solution = Solution()