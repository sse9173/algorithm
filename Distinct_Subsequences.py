# 20210919
# LeetCode

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[1,] + [0 for _ in range(len(t))] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]: dp[i][j] += dp[i - 1][j] + dp[i - 1][j - 1]
                else: dp[i][j] += dp[i - 1][j]
        return dp[len(s)][len(t)]

