# 20211122
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        p, tg = None, root
        while tg and key != tg.val:
            p = tg
            tg = tg.left if key < tg.val else tg.right
        if not tg: return root

        def recurse(cur):
            nonlocal p
            if not p: return cur
            if tg.val < p.val: p.left = cur
            else: p.right = cur
            return root

        if not tg.left: return recurse(tg.right)
        if not tg.right: return recurse(tg.left)
        rl = tg.right
        while rl.left: rl = rl.left
        rl.left = tg.left
        return recurse(tg.right)

