// Last updated: 5/29/2026, 11:52:20 AM
class Solution {
        private int firstOccurrence(int[] nums, int target) {
        int low = 0, high = nums.length - 1, res = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                res = mid;
                high = mid - 1; // keep searching left
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return res;
    }
    
    private int lastOccurrence(int[] nums, int target) {
        int low = 0, high = nums.length - 1, res = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                res = mid;
                low = mid + 1; // keep searching right
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return res;
    }
    public List<Integer> targetIndices(int[] nums, int target) {
        List<Integer> result=new ArrayList<>();
        Arrays.sort(nums);
        int first=firstOccurrence(nums,target);
        if(first==-1){
            return result;
        }
        int last=lastOccurrence(nums,target);
        for(int i=first;i<=last;i++){
            result.add(i);
        }
        return result;
    }
}