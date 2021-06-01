# 20210602
# LeetCode

class Solution:
    def dfs(self, r, c, grid):
        if r < 0 or r >= self.m or c < 0 or c >= self.n or grid[r][c] == 0: return 0
        grid[r][c] = 0
        return 1 + self.dfs(r - 1, c, grid) + self.dfs(r + 1, c, grid) + self.dfs(r, c - 1, grid) + self.dfs(r, c + 1, grid)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.ret = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    area = self.dfs(i, j, grid)
                    if self.ret < area: self.ret = area
        return self.ret
