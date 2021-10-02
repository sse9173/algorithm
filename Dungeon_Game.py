# 20211002
# LeetCode

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = min(dungeon[-1][-1], 0)
        for j in range(n - 2, -1, -1):
            dp[-1][j] = min(dungeon[-1][j] + dp[-1][j + 1], 0)
        for i in range(m - 2, -1, -1):
            dp[i][-1] = min(dungeon[i][-1] + dp[i + 1][-1], 0)
            for j in range(n - 2, -1, -1):
                dp[i][j] = min(max(dp[i + 1][j], dp[i][j + 1]) + dungeon[i][j], 0)
        return abs(dp[0][0]) + 1

