class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        vowels=['a', 'e', 'i', 'o','u']
        while i<j:
            if s[i].lower() in vowels and s[j].lower() in vowels:
                s[i],s[j] = s[j],s[i]
                i=i+1
                j=j-1
            elif s[i].lower() not in vowels and s[j].lower()in vowels:
                i+=1
            elif s[i].lower() in vowels and s[j].lower() not in vowels:
                j-=1
            else:
                i+=1
                j-=1
        return "".join(s)