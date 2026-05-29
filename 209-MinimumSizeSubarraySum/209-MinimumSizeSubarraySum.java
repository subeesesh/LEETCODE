// Last updated: 5/29/2026, 11:57:19 AM
class Solution {
    public int  minSubArrayLen(int target,int[] nums){
        int left=0,right=0,ws=0,ms=Integer.MAX_VALUE;
        for(right=0;right<nums.length;right++){
            ws+=nums[right];
            while(ws>=target){
                ms=Math.min(ms,right-left+1);
                ws-=nums[left];
                left++;
            }
        }
        if(ms==Integer.MAX_VALUE){
            return 0;
        }
        return ms;
    }
    
}