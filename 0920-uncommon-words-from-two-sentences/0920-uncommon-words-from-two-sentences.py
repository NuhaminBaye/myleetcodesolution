class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split the sentences into words
        words1 = s1.split()
        words2 = s2.split()
        
        # Count the occurrences of each word in both sentences
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        # Find uncommon words in both sentences
        uncommon_words = []
        
        for word in count1:
            if count1[word] == 1 and word not in count2:
                uncommon_words.append(word)
        
        for word in count2:
            if count2[word] == 1 and word not in count1:
                uncommon_words.append(word)
        
        return uncommon_words

# Example usage
solution = Solution()
print(solution.uncommonFromSentences("this apple is sweet", "this apple is sour"))  # Output: ["sweet", "sour"]
print(solution.uncommonFromSentences("apple apple", "banana"))  # Output: ["banana"]