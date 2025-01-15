class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        # Update the row in reverse order to avoid overwriting values
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row

# Example usage:
solution = Solution()