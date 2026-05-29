// Last updated: 5/29/2026, 11:55:43 AM
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> list=new ArrayList<>();
        if (s == null || p == null || s.length() < p.length()) return list;
        Map<Character,Integer> map=new HashMap<>();
        Map<Character,Integer> map1=new HashMap<>();
        for(int i=0;i<p.length();i++){
            map1.put(p.charAt(i),map1.getOrDefault(p.charAt(i),0)+1);
        }
        for(int i=0;i<p.length();i++){
            map.put(s.charAt(i),map.getOrDefault(s.charAt(i),0)+1);
        }
        if(map.equals(map1)){
            list.add(0);
        }
        for(int i=p.length();i<s.length();i++){
            map.put(s.charAt(i),map.getOrDefault(s.charAt(i),0)+1);
            int count=map.get(s.charAt(i-p.length()))-1;
            if(count==0) 
                map.remove(s.charAt(i-p.length()));
            else 
                map.put(s.charAt(i-p.length()),count);
            if(map.equals(map1)){
                list.add(i-p.length()+1);
            }
        }
        return list;
    }
}