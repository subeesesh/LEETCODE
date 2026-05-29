// Last updated: 5/29/2026, 11:54:17 AM
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int min=0,max=arr.length-1;
        while(min<max){
            int mid=(max+min)/2;
            if(arr[mid]>arr[mid+1]){
                max=mid;
            }
            else {
                min=mid+1;
            }
        }
        return max;
    }
}