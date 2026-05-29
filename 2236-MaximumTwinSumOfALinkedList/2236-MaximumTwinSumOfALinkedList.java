// Last updated: 5/29/2026, 11:52:17 AM
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
    public int pairSum(ListNode head) {
        ListNode fast=head,slow=head;
        ListNode prev=null,nextt;
        while(fast!=null&&fast.next!=null){
            fast=fast.next.next;
            nextt=slow.next;
            slow.next=prev;
            prev=slow;
            slow=nextt;
        }
        int max=0;
        ListNode first=prev;
        ListNode second=slow;
        while(first!=null&&second!=null){
            int sum=first.val+second.val;
            max=Math.max(max,sum);
            first=first.next;
            second=second.next;
        }
        return max;

    }
}