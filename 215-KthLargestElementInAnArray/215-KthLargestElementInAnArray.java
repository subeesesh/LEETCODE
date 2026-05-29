// Last updated: 5/29/2026, 11:57:11 AM
class Solution {
    public int findKthLargest(int[] arr, int k) {
        Arrays.sort(arr);
        return arr[arr.length-k];
    }
}