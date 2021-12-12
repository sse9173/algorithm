# 20211208
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def recurse(cur):
            nonlocal ret
            if not cur: return 0
            left, right = recurse(cur.left), recurse(cur.right)
            ret += abs(left - right)
            return (cur.val + left + right)

        recurse(root)
        return ret
