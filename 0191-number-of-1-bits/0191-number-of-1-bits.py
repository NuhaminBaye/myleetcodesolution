class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Increment count if the last bit is 1
            n >>= 1         # Right shift n by 1 to check the next bit
        return count

# Example usage:
solution = Solution()
print(solution.hammingWeight(11))            # Output: 3
print(solution.hammingWeight(128))           # Output: 1
print(solution.hammingWeight(2147483645))    # Output: 30