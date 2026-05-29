// Last updated: 5/29/2026, 11:52:26 AM
class Solution {
    public int findGCD(int[] nums) {
        Arrays.sort(nums);
        int num1 = nums[0], num2 = nums[nums.length - 1];
        int gcd = 1;
        for (int i = 1; i <= num1 && i <= num2; i++) {
            if (num1 % i == 0 && num2 % i == 0) {
                gcd = i;
            }
        }
        return gcd;
    }
}