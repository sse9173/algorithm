# 20211104
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def recurse(cur, lflag):
            if cur is None: return
            if lflag and cur.left is None and cur.right is None:
                nonlocal ret
                ret += cur.val
                return
            recurse(cur.left, True)
            recurse(cur.right, False)

        recurse(root, False)
        return ret
