// Last updated: 5/29/2026, 11:57:08 AM
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int flag=1;
        for(int i=0;i<nums.length-1;i++){
                if(nums[i]==nums[i+1]){
                    return true;
                }
        }
        return false;

    }
}