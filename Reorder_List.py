# 20211222
# LeetCode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        rev = list()
        cur = head
        while cur:
            rev.append(cur)
            cur = cur.next
        l, r = 1, len(rev) - 1
        for i in range(len(rev)):
            if i&1 == 0:
                head.next = rev[r]
                r -= 1
            else:
                head.next = rev[l]
                l += 1
            head = head.next
        head.next = None

