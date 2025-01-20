class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Check if the lengths of s and goal are the same
        if len(s) != len(goal):
            return False
        
        # If s and goal are the same, check for duplicates in s
        if s == goal:
            return len(set(s)) < len(s)  # There must be at least one duplicate
        
        # Find indices where s and goal differ
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))
        
        # There must be exactly two differences for a valid swap
        return len(diff) == 2 and diff[0] == diff[1][::-1]

# Example usage:
solution = Solution()