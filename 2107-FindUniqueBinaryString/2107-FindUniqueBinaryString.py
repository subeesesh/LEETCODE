# Last updated: 5/29/2026, 11:52:25 AM
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join(chr(ord(x[i])^1) for i, x in enumerate(nums))