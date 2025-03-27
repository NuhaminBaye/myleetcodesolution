from math import factorial

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Function to check if a number is prime
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        # Count the number of primes in the range 1 to n
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        
        # Count of non-prime numbers
        non_prime_count = n - prime_count
        
        # Calculate the number of arrangements
        arrangements = (factorial(prime_count) % MOD) * (factorial(non_prime_count) % MOD) % MOD
        
        return arrangements

# Example usage:
solution = Solution()
print(solution.numPrimeArrangements(5))  # Output: 12
print(solution.numPrimeArrangements(100))  # Output: 682289015