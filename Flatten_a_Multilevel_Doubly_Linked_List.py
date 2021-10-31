# 20211031
# LeetCode

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        stack = list()
        while cur is not None:
            if cur.child:
                if cur.next is not None: stack.append(cur.next)
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
            elif len(stack) > 0 and cur.next is None:
                cur.next = stack[-1]
                stack[-1].prev = cur
                stack.pop()
            cur = cur.next
        return head

