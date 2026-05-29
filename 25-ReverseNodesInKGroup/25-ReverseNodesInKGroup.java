// Last updated: 5/29/2026, 12:01:01 PM
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
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k == 1) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prev = dummy;
        ListNode curr, next;

        while (true) {
            curr = prev;
            for (int i = 0; i < k && curr != null; i++) curr = curr.next;
            if (curr == null) break;

            next = prev.next;

            for (int i = 1; i < k; i++) {
                ListNode temp = next.next;
                next.next = temp.next;
                temp.next = prev.next;
                prev.next = temp;
            }

            prev = next;
        }

        return dummy.next;
    }
}
