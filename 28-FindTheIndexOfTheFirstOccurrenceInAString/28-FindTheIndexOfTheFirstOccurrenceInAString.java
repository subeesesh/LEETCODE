// Last updated: 5/29/2026, 12:00:53 PM
class Solution {
    public int strStr(String haystack, String needle) {
        int n = haystack.length();
        int m = needle.length();
        
        if (m == 0) return 0; // empty needle case
        
        int i = 0, j = 0;
        while (i < n) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
                if (j == m) {
                    return i - m; 
                }
            } else {
                i = i - j + 1;
                j = 0;
            }
        }
        return -1; 
    }
}
