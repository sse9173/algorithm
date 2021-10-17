# 20211016
# LeetCode

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy0, buy1 = [0 for _ in range(len(prices) + 1)], [0 for _ in range(len(prices) + 1)]
        sell0, sell1 = [0 for _ in range(len(prices) + 1)], [0 for _ in range(len(prices) + 1)]
        buy0[0], buy1[0] = -99999, -99999
        for i in range(1, len(prices) + 1):
            p = prices[i - 1]
            buy0[i] = max(-p, buy0[i - 1])
            sell0[i] = max(p + buy0[i - 1], sell0[i - 1])
            buy1[i] = max(sell0[i - 1] - p, buy1[i - 1])
            sell1[i] = max(p + buy1[i - 1], sell1[i - 1])
        return max(sell0[-1], sell1[-1])

