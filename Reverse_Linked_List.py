# 20210907
# LeetCode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        ret, tr = ListNode(head.val), head.next
        while tr is not None:
            ret = ListNode(tr.val, ret)
            tr = tr.next
        return ret
