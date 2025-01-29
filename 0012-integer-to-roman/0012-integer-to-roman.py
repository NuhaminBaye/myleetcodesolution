class Solution:
    def intToRoman(self, num: int) -> str:
         # Mapping of integer values to their corresponding Roman numeral symbols
        value_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        roman_numeral = ''
        
        # Iterate over the value map
        for value, symbol in value_map:
            # While the current number is greater than or equal to the value
            while num >= value:
                roman_numeral += symbol  # Append the Roman numeral symbol
                num -= value  # Subtract the value from the number
        
        return roman_numeral

# Example Usage
solution = Solution()
print(solution.intToRoman(3749))  # Output: "MMMDCCXLIX"
print(solution.intToRoman(58))    # Output: "LVIII"
print(solution.intToRoman(1994))  # Output: "MCMXCIV