# 20211202
# LeetCode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: return head
        odd, even = head, head.next
        firstEven = even
        while even and even.next:
            odd.next, even.next = even.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = firstEven
        return head

