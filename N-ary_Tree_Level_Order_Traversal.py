# 20210806
# LeetCode

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        ret = [[root.val,], ]
        cur = root.children
        while True:
            elem = list()
            nxt = list()
            for tr in cur:
                elem.append(tr.val)
                nxt += tr.children
            if len(elem) == 0: return ret
            ret.append(list(elem[:]))
            cur = nxt[:]

