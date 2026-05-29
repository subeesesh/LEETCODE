# Last updated: 5/29/2026, 12:01:18 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str1=str(x)
        return str1==str1[::-1]