// Last updated: 5/29/2026, 11:53:24 AM
class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int wsum=0;
        for(int i=0;i<k;i++){
            wsum=wsum+cardPoints[i];
        }
        int max=wsum;
        for(int i=0;i<k;i++){
            wsum=wsum-cardPoints[k-i-1]+cardPoints[cardPoints.length-i-1];
            max=Math.max(max,wsum);
        }
        return max;
        
    }
}