// Last updated: 5/29/2026, 11:53:46 AM
class Solution {
    public List<String> commonChars(String[] words) {
        HashMap<Character,Integer> hs=new HashMap<>();
        for (char c : words[0].toCharArray()) {
            hs.put(c, hs.getOrDefault(c, 0) + 1);
        }
        for(int i=1;i<words.length;i++){
            HashMap<Character,Integer> hs1=new HashMap<>();
            for (char c: words[i].toCharArray()){
                hs1.put(c,hs1.getOrDefault(c,0)+1);
            }
            HashMap<Character, Integer> temp = new HashMap<>();
        for (Character c:hs.keySet()){
            if(hs1.containsKey(c)){
                temp.put(c, Math.min(hs.get(c),hs1.get(c)));
            }
        }
            hs=temp;
        }
        ArrayList<String> str = new ArrayList<>();
        for (Character c : hs.keySet()) {
            int count = hs.get(c);
            for (int i = 0; i < count; i++) {
                str.add(String.valueOf(c));
            }
        }
        return str;

    }
}