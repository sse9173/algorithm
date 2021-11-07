# 20211105
# LeetCode

class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt, i = 0, 1
        while n > 0:
            cnt += 1
            n -= i
            i += 1
        return cnt if n == 0 else cnt - 1
