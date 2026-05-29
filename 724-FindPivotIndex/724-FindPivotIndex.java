// Last updated: 5/29/2026, 11:54:43 AM
class Solution {
    public int pivotIndex(int[] nums) {
        int leftsum=0,totalsum=0;
        for(int i=0;i<nums.length;i++){
            totalsum+=nums[i];
        }
        for(int i=0;i<nums.length;i++){
            totalsum-=nums[i];
            if(leftsum==totalsum){
                return i;
            }
            else{
                leftsum+=nums[i];
            }
        }
        return -1;
    }
}