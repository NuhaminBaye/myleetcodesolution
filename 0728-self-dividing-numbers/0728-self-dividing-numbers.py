from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_numbers = []
        
        for num in range(left, right + 1):
            if self.isSelfDividing(num):
                self_dividing_numbers.append(num)
        
        return self_dividing_numbers

    def isSelfDividing(self, num: int) -> bool:
        original_num = num
        
        while num > 0:
            digit = num % 10
            if digit == 0 or original_num % digit != 0:
                return False
            num //= 10
        
        return True