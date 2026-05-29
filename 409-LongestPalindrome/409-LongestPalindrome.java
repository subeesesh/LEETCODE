// Last updated: 5/29/2026, 11:55:46 AM
class Solution {
    public int longestPalindrome(String s) {
        Map<Character,Integer> map=new HashMap<>();
        for(int i=0;i<s.length();i++){
            map.put(s.charAt(i),map.getOrDefault(s.charAt(i),0)+1);
        }
        int length=0;
        boolean ho=false;
        for(int count:map.values()){
            if(count%2==0){
                length+=count;
            }
            else{
                length+=count-1;
                ho=true;
            }
        }
        if(ho){
            length++;
        }
        return length;
    }
}