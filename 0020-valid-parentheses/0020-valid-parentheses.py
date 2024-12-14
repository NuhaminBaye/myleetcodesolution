class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():  # If it's an opening bracket
                stack.append(char)
            elif char in bracket_map.keys():  # If it's a closing bracket
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()  # Match found, pop from stack
                else:
                    return False  # No match or stack is empty
        return not stack  # Return True if stack is empty, else False

# Example usage:
solution = Solution()