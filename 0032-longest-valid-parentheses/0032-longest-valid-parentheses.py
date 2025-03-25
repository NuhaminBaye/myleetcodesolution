class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]  # Initialize the stack with -1 to handle the base case
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '(' onto the stack
            else:
                stack.pop()  # Pop the last '(' index
                if not stack:
                    stack.append(i)  # If stack is empty, push the current index
                else:
                    # Calculate the length of the valid substring
                    max_length = max(max_length, i - stack[-1])
        
        return max_length

# Example usage:
solution = Solution()
print(solution.longestValidParentheses("(()"))      # Output: 2
print(solution.longestValidParentheses(")()())"))   # Output: 4
print(solution.longestValidParentheses(""))         # Output: 0