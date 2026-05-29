// Last updated: 5/29/2026, 11:56:56 AM
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] arr = new int[n];
        int leftp = 1;
        for (int i = 0; i < n; i++) {
            arr[i] = leftp;         
            leftp *= nums[i];
        }
        int rightp = 1;
        for (int i = n - 1; i >= 0; i--) {
            arr[i] *= rightp;       
            rightp *= nums[i];
        }
        return arr;
    }
}
