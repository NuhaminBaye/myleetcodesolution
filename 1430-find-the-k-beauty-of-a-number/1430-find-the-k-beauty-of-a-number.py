class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        count = 0
        
        # Iterate through the string and extract substrings of length k
        for i in range(len(num_str) - k + 1):
            substring = num_str[i:i + k]
            divisor = int(substring)  # Convert substring to integer
            
            # Check if the divisor is valid (not zero) and if it divides num
            if divisor != 0 and num % divisor == 0:
                count += 1
                
        return count

# Example usage:
solution = Solution()