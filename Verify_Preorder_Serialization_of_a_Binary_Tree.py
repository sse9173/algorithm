# 20210826
# LeetCode

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodeN = 1
        tree = preorder.split(',')
        for node in preorder.split(','):
            nodeN -= 1
            if nodeN < 0: return False
            if node != '#': nodeN += 2
        return nodeN == 0
