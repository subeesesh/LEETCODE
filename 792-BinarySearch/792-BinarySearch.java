// Last updated: 5/29/2026, 11:54:27 AM
class Solution {
    public int search(int[] nums, int target) {
        int min=0,max=nums.length-1;
        while(min<=max){
            int mid=(max+min)/2;
            if(nums[mid]==target){
                return mid;
            }
            else if(target<nums[mid]){
                max=mid-1;
            }
            else if(target>nums[mid]){
                min=mid+1;
            }
        }
        return -1;
    }
}