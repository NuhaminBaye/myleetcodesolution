class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        # Initialize the first two steps
        first = 1  # ways to climb 1 step
        second = 2  # ways to climb 2 steps
        
        # Calculate ways for each step from 3 to n
        for i in range(3, n + 1):
            current = first + second  # the current step is the sum of the previous two
            first = second  # update first to the previous second
            second = current  # update second to the current
            
        return second  # the number of ways to climb n steps