class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # If the strings are the same, return -1
        if a == b:
            return -1
        # Otherwise, return the length of the longer string
        return max(len(a), len(b))