// Last updated: 5/29/2026, 11:56:48 AM
class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> map=new HashMap<>();
        if(s.length()!=t.length()){
            return false;
        }
            for(int i=0;i<s.length();i++){
                map.put(s.charAt(i),map.getOrDefault(s.charAt(i),0)+1);
                map.put(t.charAt(i),map.getOrDefault(t.charAt(i),0)-1);
            }
            for(int count:map.values()){
                if(count!=0){
                    return false;
                }
            }
            return true;

    }
}