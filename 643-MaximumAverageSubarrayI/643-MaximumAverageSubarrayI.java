// Last updated: 5/29/2026, 11:54:50 AM
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int n=nums.length;
        int wsum=0;
        for(int i=0;i<k;i++){
            wsum=wsum+nums[i];
        }
        double max=wsum;
        for(int i=k;i<n;i++){
            wsum=wsum+nums[i]-nums[i-k];
            max=Math.max(wsum,max);
        }
        return max/k;
    }
}