# 20210608
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def split(self, preord, inord, pidx, s, e):
        iidx = self.InPre[preord[pidx]]
        node = TreeNode(preord[pidx])
        if iidx > s: node.left = self.split(preord, inord, pidx + 1, s, iidx - 1)
        if iidx < e: node.right = self.split(preord, inord, pidx + (iidx - s + 1), iidx + 1, e)
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.InPre = dict()
        for i in range(len(inorder)): self.InPre[inorder[i]] = i
        return self.split(preorder, inorder, 0, 0, len(inorder) - 1)

