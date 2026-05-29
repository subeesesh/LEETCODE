// Last updated: 5/29/2026, 12:01:33 PM
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left=0;
        HashSet<Character> hs=new HashSet<>();
        int max_sum=0;
        for(int right=0;right<s.length();right++){
            while(hs.contains(s.charAt(right))){
                hs.remove(s.charAt(left));
                left++;
            }
            hs.add(s.charAt(right));
            max_sum=Math.max(max_sum,right-left+1);
        }
        return max_sum;

    }
}