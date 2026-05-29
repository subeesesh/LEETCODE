// Last updated: 5/29/2026, 11:55:54 AM
class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character,Integer> hm=new HashMap<>();
        char[] chars=s.toCharArray();
        for(char c: chars){
            hm.put(c,hm.getOrDefault(c,0)+1);
        }
        for (int i = 0; i < chars.length; i++) {
            if (hm.get(chars[i]) == 1) {
                return i; 
            }
        }
        return -1;
    }
}