// Last updated: 5/29/2026, 11:55:22 AM
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> st=new Stack<>();
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int i : nums2){
            while(!st.empty() && i>st.peek()){
                map.put(st.pop(),i);
            }
            st.push(i);
        }
        while(!st.empty()){
            map.put(st.pop(),-1);
        }
        for(int i=0;i<nums1.length;i++){
            nums1[i]=map.get(nums1[i]);
        }
        return nums1;
    }
}