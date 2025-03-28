class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Check if all characters are uppercase
        if word.isupper():
            return True
        # Check if all characters are lowercase
        elif word.islower():
            return True
        # Check if only the first character is uppercase
        elif word[0].isupper() and word[1:].islower():
            return True
        # If none of the above conditions are met, return False
        return False