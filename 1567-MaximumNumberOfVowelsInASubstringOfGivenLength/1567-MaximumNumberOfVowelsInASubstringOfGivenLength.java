// Last updated: 5/29/2026, 11:53:12 AM
class Solution {
    public int maxVowels(String s, int k) {
        int count=0,n=s.length();
        for(int i=0;i<k;i++){
            char c=s.charAt(i);
            if(c=='a'||c=='i'||c=='e'||c=='o'||c=='u'){
                count++;
            }
        }
        int max=count;
        for(int i=k;i<n;i++){
            char c=s.charAt(i);
            if(c=='a'||c=='i'||c=='e'||c=='o'||c=='u'){
                count++;
            }
            char ch=s.charAt(i-k);
            if(ch=='a'||ch=='i'||ch=='e'||ch=='o'||ch=='u'){
                count--;
            }
            max=Math.max(max,count);
        }
        return max;
    }
}