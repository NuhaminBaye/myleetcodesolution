class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(index: int, path: str):
            # If the current combination is complete
            if index == len(digits):
                combinations.append(path)
                return
            
            # Get the letters that the current digit maps to
            possible_letters = digit_to_letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to the current path and move to the next digit
                backtrack(index + 1, path + letter)

        combinations = []  # List to store the combinations
        backtrack(0, "")  # Start backtracking from the first digit
        return combinations