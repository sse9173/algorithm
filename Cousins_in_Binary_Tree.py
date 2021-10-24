# 20211018
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xdepth, xparent = -1, -1
        ydepth, yparent = -1, -1

        def recurse(depth, cur):
            nonlocal x, y, xdepth, xparent, ydepth, yparent
            if cur.left is not None:
                if cur.left.val == x:
                    xdepth, xparent = depth, cur.val
                elif cur.left.val == y:
                    ydepth, yparent = depth, cur.val
                else: recurse(depth + 1, cur.left)
            if cur.right is not None:
                if cur.right.val == x:
                    xdepth, xparent = depth, cur.val
                elif cur.right.val == y:
                    ydepth, yparent = depth, cur.val
                else: recurse(depth + 1, cur.right)
            if xdepth != -1 and ydepth != -1: return (xdepth == ydepth) and (xparent != yparent)

        return recurse(0, root)

