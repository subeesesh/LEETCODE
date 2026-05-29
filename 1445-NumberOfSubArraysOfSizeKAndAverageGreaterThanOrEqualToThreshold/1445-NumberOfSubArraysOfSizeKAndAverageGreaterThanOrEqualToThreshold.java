// Last updated: 5/29/2026, 11:53:26 AM
class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int n=arr.length;
        int wsum=0;
        int count=0;
        for(int i=0;i<k;i++){
            wsum+=arr[i];
        }
        int sum=wsum;
        if((int)wsum/k>=threshold){
                count++;
            }
        for(int i=k;i<n;i++){
            wsum=wsum+arr[i]-arr[i-k];
            if((int)wsum/k>=threshold){
                count++;
            }
        }
        return count;
    }
}