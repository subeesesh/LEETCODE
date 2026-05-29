# Last updated: 5/29/2026, 11:52:40 AM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence))==26