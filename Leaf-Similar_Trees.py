# 20210813
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getLeafSequence(self, cur):
        if cur is None: return []
        if cur.left is None and cur.right is None: return [cur.val, ]
        return self.getLeafSequence(cur.left) + self.getLeafSequence(cur.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeafSequence(root1) == self.getLeafSequence(root2)

