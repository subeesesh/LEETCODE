// Last updated: 5/29/2026, 11:56:37 AM
class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n=citations.length;
        for(int i=0;i<n;i++){
            if(citations[i]>=(n-i)){
                return n-i;
            }
        }
        return 0;
    }
}