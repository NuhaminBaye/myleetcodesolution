class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Function to check if str can be formed by repeating x
        def canConstruct(s, x):
            return s == x * (len(s) // len(x))
        
        # Find GCD of lengths
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Get the length of the GCD
        gcd_length = gcd(len(str1), len(str2))
        
        # Potential GCD string
        gcd_string = str1[:gcd_length]
        
        # Check if this string can construct both str1 and str2
        if canConstruct(str1, gcd_string) and canConstruct(str2, gcd_string):
            return gcd_string
        return ""

# Example usage:
solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(solution.gcdOfStrings("LEET", "CODE"))    # Output: ""