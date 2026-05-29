// Last updated: 5/29/2026, 12:00:06 PM
class Solution {
    public int lengthOfLastWord(String s) {
            String[] str = s.trim().split(" ");
            String str1 = "";
            str1=str1+str[str.length-1];
            return str1.length();           
    }
}