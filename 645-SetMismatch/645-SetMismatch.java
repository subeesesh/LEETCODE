// Last updated: 5/29/2026, 11:54:48 AM
class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int[] freq = new int[n + 1];
        int duplicate = 0;
        int missing = 0;
        for (int x : nums) {
            freq[x]++;
            if (freq[x] == 2) duplicate = x;
        }
        for (int i = 1; i <= n; i++) {
            if (freq[i] == 0) missing = i;
        }
        return new int[]{duplicate, missing};
    }
}
