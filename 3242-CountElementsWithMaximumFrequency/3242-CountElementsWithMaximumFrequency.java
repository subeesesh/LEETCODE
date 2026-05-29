// Last updated: 5/29/2026, 11:51:49 AM
class Solution {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
        }
        int max=Integer.MIN_VALUE,count=0;
        for(int i:map.values()){
            max=Math.max(max,i);
        }
        for(int i:map.values()){
            if(max==i){
                count++;

            }
        }
        return count*max;
    }
}