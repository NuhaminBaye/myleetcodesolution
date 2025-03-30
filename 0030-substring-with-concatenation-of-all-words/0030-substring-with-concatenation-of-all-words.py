from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = Counter(words)
        result_indices = []

        # Loop through each possible starting point in the string
        for i in range(len(s) - total_length + 1):
            # Get the substring to analyze
            substring = s[i:i + total_length]
            # Create a counter for the words in the substring
            substring_count = Counter()

            # Loop through each word length in the substring
            for j in range(0, total_length, word_length):
                word = substring[j:j + word_length]
                if word in word_count:
                    substring_count[word] += 1
                else:
                    break
            
            if substring_count == word_count:
                result_indices.append(i)

        return result_indices