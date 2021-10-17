# 20211011
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def recurse(cur):
            nonlocal ret
            if cur is None: return 0
            l, r = recurse(cur.left), recurse(cur.right)
            ret = max(ret, l + r)
            return max(l, r) + 1

        recurse(root)
        return ret
