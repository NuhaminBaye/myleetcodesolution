from collections import defaultdict
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Normalize the paragraph by converting it to lowercase and removing punctuation
        words = re.findall(r'\w+', paragraph.lower())
        
        # Create a dictionary to count occurrences of each word
        word_count = defaultdict(int)
        
        # Count each word, skipping banned words
        for word in words:
            if word not in banned:
                word_count[word] += 1
        
        # Find the word with the maximum count
        most_common = ""
        max_count = 0
        
        for word, count in word_count.items():
            if count > max_count:
                max_count = count
                most_common = word
        
        return most_common