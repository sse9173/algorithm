# 20211103
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def recurse(cur, val):
            if cur is None: return
            val *= 10
            if cur.left is None and cur.right is None:
                nonlocal ret
                ret += (val + cur.val)
                return
            recurse(cur.left, val + cur.val)
            recurse(cur.right, val + cur.val)

        recurse(root, 0)
        return ret

