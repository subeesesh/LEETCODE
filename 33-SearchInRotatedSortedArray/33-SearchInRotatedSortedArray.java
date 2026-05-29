// Last updated: 5/29/2026, 12:00:40 PM
class Solution {
    public int search(int[] nums, int target) {
        int min=0,max=nums.length-1;
        while(min<=max){
            int mid=(min+max)/2;
            if(nums[mid]==target){
                return mid;
            }
            else if (nums[mid]>=nums[min]){
                if(target<=nums[mid]&&target>=nums[min]){
                    max=mid-1;
                }
                else{
                    min=mid+1;
                }
            }else{
                if(target>=nums[mid]&&target<=nums[max]){
                    min=mid+1;
                }
                else{
                    max=mid-1;
                }
            }
        }
        return -1;
    }
}