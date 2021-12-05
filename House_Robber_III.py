# 20211205
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def recurse(cur):
            l, lc, r, rc = 0, 0, 0, 0
            if not cur.left and not cur.right: return (cur.val, 0)
            if cur.left: l, lc = recurse(cur.left)
            if cur.right: r, rc = recurse(cur.right)
            return (cur.val + lc + rc, max(l, lc) + max(r, rc))
        return max(recurse(root))

