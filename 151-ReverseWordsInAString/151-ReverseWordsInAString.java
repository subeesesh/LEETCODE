// Last updated: 5/29/2026, 11:58:05 AM
class Solution {
    public String reverseWords(String s) {
        String[] str=s.trim().split(" ");
        String str1="";
        for(int i=str.length-1;i>=0;i--){
            if(i==0){
                str1+=str[i];
            }
            else if(str[i]==""){
                continue;
            }
            else{
                str1+=str[i]+" ";
            }
        }
        return str1;
    }
}