// Last updated: 5/29/2026, 11:53:11 AM
class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        Arrays.sort(arr);
        int prev=arr[1]-arr[0];
        for(int i=1;i<arr.length-1;i++){
            int diff=arr[i+1]-arr[i];
            if(diff!=prev){
                return false;
            }
        }
        return true;
    }
}