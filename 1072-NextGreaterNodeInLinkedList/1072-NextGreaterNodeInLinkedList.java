// Last updated: 5/29/2026, 11:53:41 AM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        Stack<ListNode> st=new Stack<>();
        HashMap<ListNode,Integer> map=new HashMap<>();
        ListNode temp=head;
        int count=0;
        while(temp!=null){
            while(!st.empty()&&temp.val>st.peek().val){
                map.put(st.pop(),temp.val);
            }
            st.push(temp);
            temp=temp.next;
            count++;
        }
        while(!st.empty()){
            map.put(st.pop(),0);
        }
        int[] arr=new int[count];
        ListNode curr=head;
        int i=0;
        while(curr!=null){
            arr[i]=map.get(curr);
            i++;
            curr=curr.next;
        }
        return arr;
    }
}