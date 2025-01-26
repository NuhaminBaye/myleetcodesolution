class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for i in range(numRows):
            # Start with a row containing 1
            row = [1] * (i + 1)
            
            # Each triangle row (after the first) has values that are the sum of
            # the two values above it in the triangle
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            triangle.append(row)
        
        return triangle

# Example usage:
solution = Solution()
print(solution.generate(5))  # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(solution.generate(1))  # Output: [[1]]