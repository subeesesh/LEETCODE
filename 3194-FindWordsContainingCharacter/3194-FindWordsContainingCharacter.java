// Last updated: 5/29/2026, 11:51:51 AM
class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        Set<Integer> set=new HashSet<>();
        for(int i=0;i<words.length;i++){
            for(int j=0;j<words[i].length();j++){
                if(words[i].charAt(j)==x){
                    set.add(i);
                }
            }
        }
        
        List<Integer> result=new ArrayList<>(set);
        return result;
    }
}