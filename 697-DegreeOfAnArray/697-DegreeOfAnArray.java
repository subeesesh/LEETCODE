// Last updated: 5/29/2026, 11:54:44 AM
class Solution {
    public int findShortestSubArray(int[] nums) {
        int len = nums.length;
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int num : nums) {
            hm.put(num, hm.getOrDefault(num, 0) + 1);
        }
        int maxFreq = Collections.max(hm.values());
        int minLen = len;
        for (int num : hm.keySet()) {
            if (hm.get(num) == maxFreq) {
                int left = 0, right = len - 1;
                while (nums[left] != num) {
                    left++;
                }
                while (nums[right] != num) {
                    right--;
                }
                minLen = Math.min(minLen, right - left + 1);
            }
        }
        return minLen;
    }
}
