# 20211014
# LeetCode

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(2, 101):
            ps = i*i
            if ps == n: return 1
            if ps > n: break
            dp[ps] = 1
            for j in range(ps + 1, n + 1):
                dp[j] = min(dp[j], 1 + dp[j - ps])
        return dp[n]

