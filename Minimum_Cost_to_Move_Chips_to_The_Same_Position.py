# 20211206
# LeetCode

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt = [0, 0]    # idx 0 stands for odds, 1 for evens
        for pos in position: cnt[pos&1] += 1
        return min(cnt)

