// Last updated: 5/29/2026, 11:52:37 AM
class Solution {
    public int countGoodSubstrings(String s) {
        int count=0;
        for(int i=1;i<s.length()-1;i++){
            if(s.charAt(i)!=s.charAt(i-1)&&s.charAt(i)!=s.charAt(i+1)&&s.charAt(i-1)!=s.charAt(i+1)){
                count++;
            }
        }
        return count;

    }
}