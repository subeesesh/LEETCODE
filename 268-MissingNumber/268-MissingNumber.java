// Last updated: 5/29/2026, 11:56:41 AM
public class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        HashSet<Integer> hs = new HashSet<>();
        for (int i = 0; i <= n; i++) {
            hs.add(i);
        }
        for (int num : nums) {
            hs.remove(num);
        }
        return hs.iterator().next();
    }
}
