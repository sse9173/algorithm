# 20211017
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ret = 0

        def recurse(cur, rangeSum):
            nonlocal targetSum, ret
            if cur is None: return
            for i in range(len(rangeSum)):
                rangeSum[i] += cur.val
                if rangeSum[i] == targetSum: ret += 1
            if cur.val == targetSum: ret += 1
            recurse(cur.left, rangeSum + [cur.val, ])
            recurse(cur.right, rangeSum + [cur.val, ])

        recurse(root, [])
        return ret

