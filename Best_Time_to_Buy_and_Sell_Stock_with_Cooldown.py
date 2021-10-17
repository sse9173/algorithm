# 20211015
# LeetCode

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        if len(prices) == 2: return 0 if prices[0] >= prices[1] else prices[1] - prices[0]
        dp = [[0 for _ in range(len(prices))] for _ in range(len(prices))]
        dp[0][0], dp[0][1] = 0, -prices[0]
        dp[1][0] = max(dp[0][1] + prices[1], dp[0][0])
        dp[1][1] = max(dp[0][0] - prices[1], dp[0][1])
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1])
        return dp[-1][0]

