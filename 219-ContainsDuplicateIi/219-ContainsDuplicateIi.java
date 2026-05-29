// Last updated: 5/29/2026, 11:57:16 AM
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(map.containsKey(nums[i])){
                if(Math.abs(i-map.get(nums[i]))<=k){
                    return true;
                }
            }
            map.put(nums[i],i);
        }
        return false;
    }
}