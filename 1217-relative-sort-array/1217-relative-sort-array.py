from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Create a dictionary to store the order of elements in arr2
        order_map = {value: index for index, value in enumerate(arr2)}
        
        # Split arr1 into two parts: ones that are in arr2 and others
        in_arr2 = []
        not_in_arr2 = []
        
        for num in arr1:
            if num in order_map:
                in_arr2.append(num)
            else:
                not_in_arr2.append(num)
        
        # Sort the elements that are not in arr2
        not_in_arr2.sort()
        
        # Sort the elements that are in arr2 based on their order in arr2
        in_arr2.sort(key=lambda x: order_map[x])
        
        # Combine the two lists
        return in_arr2 + not_in_arr2

# Example usage:
solution = Solution()
print(solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))  
# Output: [2,2,2,1,4,3,3,9,6,7,19]
print(solution.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))  
# Output: [22,28,8,6,17,44] 