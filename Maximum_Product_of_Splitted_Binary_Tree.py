# 20210819
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = list()

        def recurse(cur):
            if cur is None: return 0
            cur.val += (recurse(cur.left) + recurse(cur.right))
            sums.append(cur.val)
            return cur.val

        target = recurse(root)//2
        near = sums[0]
        ndiff = abs(near - target)
        if ndiff == 0: return (near*(root.val - near))%1000000007
        for s in sums[1:]:
            if abs(s - target) < ndiff:
                near = s
                ndiff = abs(near - target)
                if ndiff == 0: return (near*(root.val - near))%1000000007
        return (near*(root.val - near))%1000000007

