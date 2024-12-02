class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        x = 0
        while (2 ** x) <= n:
            if n == 2 ** x:
                return True
            x += 1
        return False