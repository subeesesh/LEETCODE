# Last updated: 5/29/2026, 12:00:54 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k==1:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while True:
            curr=prev
            for i in range(k):
                if curr is not None:
                    curr=curr.next
            if curr is None:
                break
            next=prev.next
            for i in range(1,k):
                temp=next.next
                next.next=temp.next
                temp.next=prev.next
                prev.next=temp
            prev=next
        return dummy.next