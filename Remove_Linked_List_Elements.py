# 20211112
# LeetCode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val: head = head.next
        if head is None: return head
        cur = head
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else: cur = cur.next
        return head

