# 20210830
# LeetCode

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mina, minb = m, n
        for op in ops:
            mina = min(mina, op[0])
            minb = min(minb, op[1])
        return mina*minb

