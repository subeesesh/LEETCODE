// Last updated: 5/29/2026, 11:56:57 AM
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
    public boolean isPalindrome(ListNode head) {
        if(head==null||head.next==null) return true;
        ListNode fast=head,slow=head;
        ListNode prev=null,nextt;
        while(fast!=null&&fast.next!=null){
            fast=fast.next.next;
            nextt=slow.next;
            slow.next=prev;
            prev=slow;
            slow=nextt;
        }
        if(fast!=null){
            slow=slow.next;
        }
        ListNode first=prev;
        ListNode second=slow;
        while(first!=null&&second!=null){
            if(first.val!=second.val){
                return false;
            }
            first=first.next;
            second=second.next;
        }
        return true;
    }
}