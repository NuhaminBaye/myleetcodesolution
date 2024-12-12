class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate through each character in the string
        for char in reversed(s):
            value = roman_map[char]
            
            # Determine if we need to add or subtract the value
            if value < prev_value:
                total -= value
            else:
                total += value
                
            # Update the previous value
            prev_value = value
        
        return total  