# 20210902
# LeetCode

# *** Not Optimized

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        ret = list()
        n += 1

        def compare(t1, t2):
            if t1 is None and t2 is None: return True
            if t1.val == t2.val:
                return compare(t1.left, t2.left) and compare(t1.right, t2.right)
            else: return False


        def recurse(root, v):
            if len(v) == n - 1:
                for tree in ret:
                    if compare(tree, root) is True: break
                else: ret.append(copy.deepcopy(root))
                return
            for i in range(1, n):
                if i not in v:
                    v.append(i)
                    node = root
                    while True:
                        if node.val > i:
                            if node.left is None:
                                node.left = TreeNode(i)
                                recurse(root, v)
                                node.left = None
                                break
                            else: node = node.left
                        else:
                            if node.right is None:
                                node.right = TreeNode(i)
                                recurse(root, v)
                                node.right = None
                                break
                            else: node = node.right
                    v.pop()

        for i in range(1, n):
            recurse(TreeNode(i), [i,])

        return ret
