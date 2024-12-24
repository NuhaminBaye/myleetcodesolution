class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        length = len(flowerbed)

        while i < length:
            # Check if the current plot is empty and the adjacent plots are also empty
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1  # Plant a flower
                count += 1
            i += 1  # Move to the next plot

            # If we've already planted enough flowers, return true
            if count >= n:
                return True

        return count >= n  # Check if we managed to plant at least n flowers