// Last updated: 5/29/2026, 11:52:10 AM
class Solution {
    public int minimumRecolors(String blocks, int k) {
        int min=Integer.MAX_VALUE,count=0,n=blocks.length();
        for(int i=0;i<k;i++){
            if(blocks.charAt(i)=='W'){
                count++;
            }
        }
        min=count;
        for(int i=k;i<n;i++){
            if(blocks.charAt(i)=='W'){
                count++;
            }
            if(blocks.charAt(i-k)=='W'){
                count--;
            }
            min=Math.min(min,count);
        }
        return min;
    }
}