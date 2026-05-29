// Last updated: 5/29/2026, 11:52:18 AM
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
    public ListNode deleteMiddle(ListNode head) {
        if (head.next == null) return null;
        ListNode fast=head;
        ListNode slow=head;
        ListNode prev=null;
        while(fast!=null&&fast.next!=null){
            prev=slow;
            fast=fast.next.next;
            slow=slow.next;
        }
        prev.next=slow.next;
        return head;
    }
}