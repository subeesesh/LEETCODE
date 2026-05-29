# Last updated: 5/29/2026, 11:59:58 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        tail=head
        length=1
        while tail.next is not None:
            tail=tail.next
            length+=1
        tail.next=head
        k%=length
        if k==0:
            tail.next=None
            return head
        curr=head
        for i in range(length-k-1):
            curr=curr.next
        newhead=curr.next
        curr.next=None
        return newhead

        