// Last updated: 5/29/2026, 11:55:04 AM
class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer,Integer> map=new HashMap<>();
        map.put(0,1);
        int ps=0,count=0;
        for(int i=0;i<nums.length;i++){
            ps+=nums[i];
            if(map.containsKey(ps-k)){
                count+=map.get(ps-k);
            }
            map.put(ps, map.getOrDefault(ps, 0) + 1);
        }
        return count;
    }
}