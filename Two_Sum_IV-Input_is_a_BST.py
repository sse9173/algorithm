# 20210823
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        v = set()

        def recurse(cur):
            if cur is None: return False
            if k - cur.val in v: return True
            v.add(cur.val)
            return recurse(cur.left) or recurse(cur.right)

        return recurse(root)
