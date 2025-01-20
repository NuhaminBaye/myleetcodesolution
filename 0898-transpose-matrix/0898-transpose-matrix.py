class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns in the original matrix
        m = len(matrix)
        n = len(matrix[0])
        
        # Create a new matrix for the transposed result
        transposed = [[0] * m for _ in range(n)]
        
        # Fill the transposed matrix
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        
        return transposed

# Example usage:
solution = Solution()
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result1 = solution.transpose(matrix1)
print(result1)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

matrix2 = [[1, 2, 3], [4, 5, 6]]
result2 = solution.transpose(matrix2)
print(result2)  # Output: [[1, 4], [2, 5], [3, 6]]