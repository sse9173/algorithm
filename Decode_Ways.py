# 20210818
# LeetCode

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        if s[0] != '0': dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0': dp[i] += dp[i - 1]
            if s[i - 2] != '0' and 0 < int(s[i - 2:i]) <= 26: dp[i] += dp[i - 2]
        return dp[len(s)]
