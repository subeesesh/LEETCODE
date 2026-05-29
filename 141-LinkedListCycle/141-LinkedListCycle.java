// Last updated: 5/29/2026, 11:58:23 AM
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head==null||head.next==null){
            return false;
        }
        HashMap<ListNode,Integer> map=new HashMap<>();
        ListNode curr=head;
        while(curr!=null){
            if(map.containsKey(curr)){
                return true;
            }
            map.put(curr,curr.val);
            curr=curr.next;
        }
        return false;
    }
}