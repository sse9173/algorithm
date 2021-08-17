# 20210817
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, cur, pmax):
        if cur is None: return 0
        if cur.val >= pmax:
            return 1 + self.recurse(cur.left, cur.val) + self.recurse(cur.right, cur.val)
        else: return self.recurse(cur.left, pmax) + self.recurse(cur.right, pmax)

    def goodNodes(self, root: TreeNode) -> int:
        return self.recurse(root, -99999)
