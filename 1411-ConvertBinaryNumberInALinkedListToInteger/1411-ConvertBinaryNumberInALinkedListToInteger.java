// Last updated: 5/29/2026, 11:53:27 AM
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
    public int getDecimalValue(ListNode head) {
        int num=0;
        ListNode curr=head;
        while(curr!=null){
            num=(num<<1)|curr.val;
            curr=curr.next;
        }
        return num;
    }
}