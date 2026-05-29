# Last updated: 5/29/2026, 11:51:22 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        parivontel = s
        vowels = set('aeiou')
        words = parivontel.split()
        first_vowel_count = sum(1 for ch in words[0] if ch in vowels)
        for i in range(1, len(words)):
            vowel_count = sum(1 for ch in words[i] if ch in vowels)
            if vowel_count == first_vowel_count:
                words[i] = words[i][::-1]
        
        return " ".join(words)
