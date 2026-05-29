// Last updated: 5/29/2026, 12:01:19 PM
class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int max = 0;
        while (left < right) {
            int width = right - left;
            int h = Math.min(height[left], height[right]);
            int water = h * width;
            max = Math.max(max, water);
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return max;
    }
}
