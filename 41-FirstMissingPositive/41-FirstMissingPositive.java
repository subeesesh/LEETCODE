// Last updated: 5/29/2026, 12:00:38 PM
class Solution {
    public int firstMissingPositive(int[] nums) {
        int len=nums.length;
        HashSet<Integer> hs= new HashSet<>();
        for(int i=0;i<nums.length;i++){
            hs.add(nums[i]);
        }
        for(int i=1;i<=nums.length;i++){
            if(!hs.contains(i)){
                return i;
            }
        }
        return len+1;
    }
}