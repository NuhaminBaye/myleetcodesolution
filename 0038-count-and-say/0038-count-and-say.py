class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Recursive case
        previous = self.countAndSay(n - 1)
        result = []
        count = 1
        
        for i in range(1, len(previous)):
            if previous[i] == previous[i - 1]:
                count += 1
            else:
                # Append the count and the digit to the result
                result.append(str(count))
                result.append(previous[i - 1])
                count = 1  # Reset count for the new digit
        
        # Handle the last group
        result.append(str(count))
        result.append(previous[-1])
        
        return ''.join(result)

# Example usage:
solution = Solution()
print(solution.countAndSay(1))  # Output: "1"
print(solution.countAndSay(4))  # Output: "1211"