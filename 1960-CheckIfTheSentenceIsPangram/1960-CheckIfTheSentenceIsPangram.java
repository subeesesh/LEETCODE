// Last updated: 5/29/2026, 11:52:46 AM
class Solution {
    public boolean checkIfPangram(String sentence) {
        sentence =sentence.toLowerCase();
        HashSet<Character> hs=new HashSet<>();
        for(int i=0;i<sentence.length();i++){
            if(sentence.charAt(i)>='a'&&sentence.charAt(i)<='z'){
                hs.add(sentence.charAt(i));
            }
        }
        if(hs.size()==26){
            return true;
        }
        else{
            return false;
        }
    }
}