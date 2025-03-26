class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False  # Perfect numbers are greater than 1
        
        divisor_sum = 1  # Start with 1 because it's a divisor of every number
        
        # Check for divisors from 2 up to the square root of num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # If i is a divisor
                divisor_sum += i
                if i != num // i:  # Avoid adding the square root twice
                    divisor_sum += num // i
        
        # Check if the sum of divisors equals the original number
        return divisor_sum == num

# Example usage:
solution = Solution()
print(solution.checkPerfectNumber(28))  # Output: True
print(solution.checkPerfectNumber(7))   # Output: False    