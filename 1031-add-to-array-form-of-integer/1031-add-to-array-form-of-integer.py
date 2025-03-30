from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # Initialize the result list and carry
        result = []
        carry = 0

        # Start adding from the least significant digit
        n = len(num)
        for i in range(n - 1, -1, -1):
            # Add current digit and the corresponding digit from k
            digit_sum = num[i] + (k % 10) + carry
            carry = digit_sum // 10  # Update carry for next iteration
            result.append(digit_sum % 10)  # Append the last digit to the result
            k //= 10  # Remove the last digit from k
        
        # If there are remaining digits in k
        while k > 0:
            digit_sum = (k % 10) + carry
            carry = digit_sum // 10
            result.append(digit_sum % 10)
            k //= 10
        
        # If there's still a carry left
        if carry > 0:
            result.append(carry)
        
        # Reverse the result to get the correct order
        return result[::-1]