// Last updated: 5/29/2026, 12:01:08 PM
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums); 
        Set<List<Integer>> result = new HashSet<>();
        int n = nums.length;
        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; 
            int target = -nums[i];
            HashSet<Integer> seen = new HashSet<>();
            for (int j = i + 1; j < n; j++) {
                int complement = target - nums[j];
                if (seen.contains(complement)) {
                    result.add(Arrays.asList(nums[i], complement, nums[j])); // Already sorted
                }
                seen.add(nums[j]);
            }
        }
        return new ArrayList<>(result);
    }
}
