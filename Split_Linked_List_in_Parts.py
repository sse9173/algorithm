# 20210929
# LeetCode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        total, curnode = 0, head
        while curnode is not None:
            total += 1
            curnode = curnode.next
        ret = list()
        cnt, curnode = total//k, head
        for i in range(total%k):
            ret.append(curnode)
            for j in range(cnt): curnode = curnode.next
            tmp = curnode
            curnode = curnode.next
            tmp.next = None
        while curnode is not None:
            ret.append(curnode)
            for j in range(cnt - 1): curnode = curnode.next
            tmp = curnode
            curnode = curnode.next
            tmp.next = None
        while len(ret) < k: ret.append(None)
        return ret

