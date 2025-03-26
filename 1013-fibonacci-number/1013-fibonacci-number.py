class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        # Initialize the first two Fibonacci numbers
        a, b = 0, 1
        
        # Iterate from 2 to n
        for _ in range(2, n + 1):
            a, b = b, a + b  # Update a and b to the next Fibonacci numbers
        
        return b  # b is F(n)

# Example usage:
solution = Solution()
print(solution.fib(2))  # Output: 1
print(solution.fib(3))  # Output: 2
print(solution.fib(4))  # Output: 3