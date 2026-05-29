// Last updated: 5/29/2026, 11:51:32 AM
class Solution {
    private static final int MOD = 1_000_000_007;

    public int specialTriplets(int[] nums) {
        int n = nums.length;
        long ans = 0;

        HashMap<Integer, Long> left = new HashMap<>();
        HashMap<Integer, Long> right = new HashMap<>();

        // Build right frequency map
        for (int num : nums) {
            right.put(num, right.getOrDefault(num, 0L) + 1);
        }

        // j = middle index
        for (int j = 0; j < n; j++) {
            int mid = nums[j];

            // Remove current mid from right
            right.put(mid, right.get(mid) - 1);
            if (right.get(mid) == 0) right.remove(mid);

            int target = 2 * mid;

            long leftCount = left.getOrDefault(target, 0L);
            long rightCount = right.getOrDefault(target, 0L);

            ans = (ans + (leftCount * rightCount) % MOD) % MOD;

            // Add current mid to left
            left.put(mid, left.getOrDefault(mid, 0L) + 1);
        }

        return (int) ans;
    }
}
