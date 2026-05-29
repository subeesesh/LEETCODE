// Last updated: 5/29/2026, 12:00:12 PM
class Solution {
    public int maxSubArray(int[] nums) {
        int max_ele=nums[0];
        int max_far=nums[0];
        for(int i=1;i<nums.length;i++){
            max_ele=Math.max(nums[i],max_ele+nums[i]);
            max_far=Math.max(max_far,max_ele);
        }
        return max_far;
    }
}