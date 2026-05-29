# Last updated: 5/29/2026, 12:00:45 PM
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        ans = []
        for i in range(len(s) - total_len + 1):
            seen = {}
            valid = True
            for j in range(total_words):
                start = i + j * word_len
                word = s[start:start + word_len]
                if word not in word_count:
                    valid = False
                    break
                if word in seen:
                    seen[word] += 1
                else:
                    seen[word] = 1
                if seen[word] > word_count[word]:
                    valid = False
                    break
            if valid:
                ans.append(i)
        return ans