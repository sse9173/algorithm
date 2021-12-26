# 20211215
# LeetCode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        cur = head
        while cur:
            nnode = cur.next
            node = ret
            while node.next and cur.val > node.next.val: node = node.next
            node.next, cur.next = cur, node.next
            cur = nnode
        return ret.next
