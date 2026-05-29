# Last updated: 5/29/2026, 11:59:20 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head, x):
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        
        left = left_dummy
        right = right_dummy
        curr = head
        
        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next
            curr = curr.next
        
        right.next = None          # important!
        left.next = right_dummy.next
        
        return left_dummy.next

        