# 20210804
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ret = list()

    def recurse(self, cur, tg, csum, elem):
        if cur.left is not None: self.recurse(cur.left, tg, csum + cur.val, elem + [cur.val, ])
        if cur.right is not None: self.recurse(cur.right, tg, csum + cur.val, elem + [cur.val, ])
        if cur.left is None and cur.right is None and csum + cur.val == tg:
            self.ret.append(elem + [cur.val, ])

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None: return list()
        self.ret = list()
        self.recurse(root, targetSum, 0, [])
        return self.ret

