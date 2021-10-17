# 20211013
# LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(preorder[0])
        stack = [head, ]
        cur = head
        for val in preorder[1:]:
            if val < cur.val:
                cur.left = TreeNode(val)
                cur = cur.left
                stack.append(cur)
            else:
                while len(stack) > 0 and stack[-1].val < val: cur = stack.pop()
                cur.right = TreeNode(val)
                cur = cur.right
                stack.append(cur)
        return head

