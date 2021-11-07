# 20211102
# LeetCode

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cost = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: cost += 1
                elif grid[i][j] == 1: start = (i, j)
                elif grid[i][j] == 2: tg = (i, j)

        def recurse(y, x, cnt):
            nonlocal grid, tg, m, n
            if (y, x) == tg: return int(cnt == 0)
            ret = 0
            if y > 0 and grid[y - 1][x] >= 0:
                grid[y - 1][x] = -2
                ret += recurse(y - 1, x, cnt - 1)
                grid[y - 1][x] = 0
            if x < n - 1 and grid[y][x + 1] >= 0:
                grid[y][x + 1] = -2
                ret += recurse(y, x + 1, cnt - 1)
                grid[y][x + 1] = 0
            if y < m - 1 and grid[y + 1][x] >= 0:
                grid[y + 1][x] = -2
                ret += recurse(y + 1, x, cnt - 1)
                grid[y + 1][x] = 0
            if x > 0 and grid[y][x - 1] >= 0:
                grid[y][x - 1] = -2
                ret += recurse(y, x - 1, cnt - 1)
                grid[y][x - 1] = 0
            return ret

        grid[start[0]][start[1]] = -2
        return recurse(start[0], start[1], cost + 1)

