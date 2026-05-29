// Last updated: 5/29/2026, 11:59:44 AM
class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        
        while (mid <= high) {
            if (nums[mid] == 0) {
                // swap nums[low] and nums[mid]
                int tmp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = tmp;
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else { // nums[mid] == 2
                // swap nums[mid] and nums[high]
                int tmp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = tmp;
                high--;
            }
        }
    }
}
