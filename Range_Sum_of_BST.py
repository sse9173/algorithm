# 20211214
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ret = 0

        def search(cur):
            nonlocal low, high, ret
            if not cur: return
            if low <= cur.val <= high:
                ret += cur.val
                search(cur.left)
                search(cur.right)
            elif cur.val < low: search(cur.right)
            elif cur.val > high: search(cur.left)

        search(root)
        return ret

